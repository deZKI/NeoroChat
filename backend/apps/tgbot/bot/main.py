from django.conf import settings
from aiogram import Bot, Dispatcher, types, filters, enums

from ai.gigachat import GigaChatService
from apps.tgbot.models import ChatHistory
from apps.users.models import UserExtended

from .middlewares import AuthMiddleware

TOKEN = settings.TELEGRAM_BOT_API_TOKEN

bot = Bot(token=TOKEN)

dp = Dispatcher()
dp.message.outer_middleware(AuthMiddleware())


@dp.message(filters.Command("start"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Отправь мне любой запрос, и я постараюсь помочь.")


@dp.message()
async def handle_message(message: types.Message):
    user = message.from_user
    user_id = user.id
    user_query = message.text  # Запрос пользователя

    # Отправляем запрос в GigaChat
    response = GigaChatService.get_response(user_query)

    user = await UserExtended.objects.aget(
        username=user_id
    )
    # Сохраняем запрос и ответ в базу данных
    await ChatHistory.objects.acreate(
        user=user,
        request_text=user_query,
        response_text=response
    )

    # Отправляем ответ пользователю
    await message.reply(f"Ответ GigaChat: {response}", parse_mode=enums.ParseMode.MARKDOWN)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command="/start", description="Запустить"),
    ]
    await bot.set_my_commands(commands)


async def start_bot():
    await set_commands(bot)
    await bot.delete_webhook()
    await dp.start_polling(bot)
