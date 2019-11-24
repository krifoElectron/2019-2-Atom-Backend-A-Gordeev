from django.db import models


class Member(models.Model):
    user = models.ForeignKey(
        'user_profile.User',
        on_delete=models.SET_NULL, null=True, related_name='members')
    chat = models.ForeignKey(
        'chats.Chat',
        on_delete=models.SET_NULL, null=True, related_name='members')
    new_messages = models.IntegerField(default=0)
    last_read_message = models.ForeignKey(
        'chats.Message',
        on_delete=models.SET_NULL, null=True, related_name='members')
