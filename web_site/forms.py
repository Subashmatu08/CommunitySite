from web_site.models import Blog, CodeGist
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomAuthenticateForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder' : 'Github ID'})
        self.fields['password'].widget = forms.TextInput(attrs={'placeholder' : 'password', 'type' : 'password'})

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name', "last_name", 'username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget = forms.TextInput(attrs={"placeholder" : "First Name", "classname" : "form-control"})
        self.fields["last_name"].widget = forms.TextInput(attrs={"placeholder" : "Last Name"})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder' : 'Github ID'})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder' : 'Email'})
        self.fields['password1'].widget = forms.TextInput(attrs={'placeholder' : 'Password', 'type' : 'password'})
        self.fields['password2'].widget = forms.TextInput(attrs={'placeholder' : 'Confirm Password', 'type' : 'password'})


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "description", "content")

class CodeGistForm(forms.ModelForm):
    class Meta:
        model = CodeGist
        fields = ("coding_platform", "problem_url", "language", "analogy", "code_snippet",)