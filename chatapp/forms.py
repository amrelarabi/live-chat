from django import forms


class SignUpForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    f_name = forms.CharField(label='First name', max_length=30)
    l_name = forms.CharField(label='Last name', max_length=30)
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    re_password = forms.CharField(label='RePassword', widget=forms.PasswordInput())


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    username = forms.CharField(label='Username', max_length=30)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

