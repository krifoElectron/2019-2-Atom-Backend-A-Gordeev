from django.contrib import admin

from chats.models import Chat


class ChatAdmin(admin.ModelAdmin):
    pass


admin.site.register(Chat, ChatAdmin)
