from django import forms
from django.contrib import admin
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext, gettext_lazy as _

from usuarios.models import CustomUser, Student
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.

class CustomUserCreationForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(
        label="Password confirmation", widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = ["email", "name", "first_surname", "second_surname", "rol"]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Raw passwords are not stored, so there is no way to see this "
            "user’s password, but you can change the password using "
            '<a href="{}">this form</a>.'
        ),
    )

    class Meta:
        model = CustomUser
        fields = "__all__"
        field_classes = {"username": 'email'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = password.help_text.format("../password/")
        user_permissions = self.fields.get("user_permissions")
        if user_permissions:
            user_permissions.queryset = user_permissions.queryset.select_related(
                "content_type"
            )

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "name", "rol"]
    list_filter = ["email", "rol", "name"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "first_surname", "second_surname"]}),
        ("Permissions", {"fields": ["rol", "groups"]}),
        ("Company", {"fields": ["company"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(CustomUser, UserAdmin)
admin.site.register(Student)