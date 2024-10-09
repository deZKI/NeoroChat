from typing import Callable, Any, Awaitable

from django.db.utils import IntegrityError

from aiogram import types
from aiogram import BaseMiddleware

from apps.users.models import UserExtended


class AuthMiddleware(BaseMiddleware):
    async def __call__(self,
                       handler: Callable[[types.TelegramObject, dict[str, Any]], Awaitable[Any]],
                       event: types.TelegramObject | types.Message,
                       data: dict[str, Any]) -> Any:
        tg_user = event.from_user if event.message_id else event.callback_query.from_user
        try:
            user, created = await UserExtended.objects.aget_or_create(
                username=tg_user.id,
                defaults={
                    'first_name': tg_user.first_name if tg_user.first_name else 'Неизвестно',
                    'last_name': tg_user.last_name if tg_user.last_name else 'Неизвестно',
                }
            )

        except IntegrityError:
            user = await UserExtended.objects.filter(username=tg_user.id).afirst()
            user.username = tg_user.id
            user.first_name = tg_user.first_name if tg_user.first_name else 'Неизвестно'
            user.last_name = tg_user.last_name if tg_user.last_name else 'Неизвестно'
            await user.asave(update_fields=['username', 'first_name', 'last_name'])

        data['user'] = user  # Сохраняем пользователя в data

        return await handler(event, data)
