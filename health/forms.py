# health/forms.py
from django import forms
from .models import Article, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('content',)


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser