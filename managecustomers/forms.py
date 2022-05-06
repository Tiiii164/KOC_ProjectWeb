
from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
        }

        widgets = {
            "username": forms.TextInput(attrs={
                "required": True,

                "class": "form-control mt-1 mb-3",
                "placeholder": "Enter UserName here ...",

            }
            ),
            "password": forms.PasswordInput(attrs={
                "required": True,
                "class": "form-control",
                "placeholder": "Enter password here ...",
            }
            ),
            "email": forms.EmailInput(attrs={
                "required": True,
                "class": "form-control",
                "placeholder": "Enter email here ...",
            }
            ),
            "first_name": forms.TextInput(attrs={
                "required": False,

                "class": "form-control mt-1 mb-3",
                "placeholder": "Enter UserName here ...",

            }
            ),
            "last_name": forms.TextInput(attrs={
                "required": False,

                "class": "form-control mt-1 mb-3",
                "placeholder": "Enter UserName here ...",

            }
            ),

        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {

            "email",
            "first_name",
            "last_name",
        }

        widgets = {

            "email": forms.EmailInput(attrs={
                "required": True,
                "class": "form-control",
                "placeholder": "Enter email here ...",
            }
            ),
            "first_name": forms.TextInput(attrs={
                "required": False,

                "class": "form-control mt-1 mb-3",
                "placeholder": "Enter UserName here ...",

            }
            ),
            "last_name": forms.TextInput(attrs={
                "required": False,

                "class": "form-control mt-1 mb-3",
                "placeholder": "Enter UserName here ...",

            }
            ),

        }
