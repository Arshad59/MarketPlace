from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('content',)
        widget = {
            'content':forms.Textarea(
                attrs={
                    'class':'w-1/2 py-4 px-6 rounded-xl border',
                    
                }
            )
        }