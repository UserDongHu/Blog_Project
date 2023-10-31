from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class CreateUserForm(UserCreationForm):
    nickname = forms.CharField(max_length=20)
    
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'nickname', 'password1', 'password2']
        
    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if not nickname:
            raise forms.ValidationError("Nickname is required")
        return nickname