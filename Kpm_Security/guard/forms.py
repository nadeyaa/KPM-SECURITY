from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfileImageForm(forms.Form):
    profile_image = forms.ImageField()

class RegisterForm(UserCreationForm):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('security_guard', 'Security Guard'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        user.role = self.cleaned_data['role']
        if commit:
            user.save()
        return user