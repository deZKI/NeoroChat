from django.contrib import admin

from apps.tgbot.models import ChatHistory


@admin.register(ChatHistory)
class ChatHistoryAdmin(admin.ModelAdmin):
    pass
