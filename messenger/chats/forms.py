from django import forms
 
class MessageForm(forms.Form):
    user_id = forms.IntegerField()
    chat_id = forms.IntegerField()
    text = forms.CharField()
