from django import forms


class TodoForm(forms.Form):
    text = forms.CharField(max_length=40,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Do DS lab and press enter',
                                      'aria-label': 'Todo', 'aria-describedby': 'add-btn'}))


class RegisterForm(forms.Form):

    email = forms.CharField(max_length=40,
                            widget=forms.TextInput(
                                attrs={'id': 'email', 'type': 'email'}))
    password = forms.CharField(max_length=40,
                               widget=forms.PasswordInput(
                                 attrs={'id': 'password', 'type': 'password'}))

    submit = forms.CharField(max_length=40,
                             widget=forms.TextInput(
                                 attrs={'id': 'submit', 'type': 'submit', 'value': 'Register'}))


class LoginForm(forms.Form):

    email = forms.CharField(max_length=40,
                            widget=forms.TextInput(
                                attrs={'id': 'email', 'type': 'email'}))
    password = forms.CharField(max_length=40,
                               widget=forms.PasswordInput(
                                 attrs={'id': 'password', 'type': 'password'}))

    submit = forms.CharField(max_length=40,
                             widget=forms.TextInput(
                                 attrs={'id': 'submit', 'type': 'submit', 'value': 'Login'}))
