from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    username = forms.CharField(max_length=10, required=True, help_text='Enter your roll number (Eg. 16uec001).')
    email = forms.EmailField(max_length=120, required=True, help_text='Enter your email with domain name @lnmiit.ac.in')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def check_email(self):
        email = self.cleaned_data.get['email']
        base, provider = email.split("@")
        if provider != "lnmiit.ac.in":
            raise forms.ValidationError("Domain name is not @lnmiit.ac.in")
        return email
