from django.db import models


class Message(models.Model):
    text = models.TextField(default='')
    added_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'user_profile.User',
        on_delete=models.SET_NULL, null=True, related_name='messages')
    chat = models.ForeignKey(
        'chats.Chat',
        on_delete=models.SET_NULL, null=True, related_name='messages')


class Chat(models.Model):
    title = models.CharField(max_length=128, blank=False)
    is_group_chat = models.BooleanField(default=False)
    last_message = models.ForeignKey(
        'chats.Message',
        on_delete=models.SET_NULL, null=True, related_name='messages')


class Attachment(models.Model):
    attach_type = models.CharField(max_length=32, blank=False)
    message = models.ForeignKey(
        'chats.Message', on_delete=models.SET_NULL,
        null=True, related_name='attachs')
    chat = models.ForeignKey(
        Chat, on_delete=models.SET_NULL, null=True, related_name='attachs')
    user = models.ForeignKey(
        'user_profile.User',
        on_delete=models.SET_NULL, null=True, related_name='attachs')
    url = models.CharField(max_length=256, blank=False, default='/')
