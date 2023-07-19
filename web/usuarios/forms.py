from django import forms


class NameForm(forms.Form):
    GENDERS = [
    ('M', 'Mujer'),
    ('H', 'Hombre'),
]
    email = forms.EmailField(label='Ingresa tu email', max_length=100)
    name = forms.CharField(label='Nombre', max_length=100)
    password = forms.CharField(label='Password', max_length=30)
    gender = forms.ChoiceField(choices=GENDERS)
    photo = forms.ImageField()


class LoginForm(forms.Form):
    email = forms.EmailField(label="Ingresa tu email")
    password = forms.CharField(widget=forms.PasswordInput)
