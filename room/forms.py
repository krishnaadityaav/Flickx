from django import forms
from django.contrib.auth.models import User
from .models import Room,JoinRequest
class InvitationForm(forms.Form):
    chat_room = forms.CharField(label='Chat Room Name')
    password = forms.CharField(widget=forms.PasswordInput())
    invitees = forms.ModelMultipleChoiceField(queryset=User.objects.all(), widget=forms.CheckboxSelectMultiple)

class JoinRequestForm(forms.ModelForm):
    req_room = forms.CharField(label='Room name',widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = JoinRequest
        fields = ['req_room', 'password']