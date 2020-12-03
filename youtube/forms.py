from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=300)
    password = forms.CharField(label='Password', max_length=300)

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=300)
    password = forms.CharField(label='Password', max_length=20)
    email = forms.CharField(label='Email', max_length=300)

class CommentForm(forms.Form):
    text = forms.CharField(label='Text', max_length=500)
    #video = forms.IntegerField(widget=forms.HiddenInput(), initial=1) 
    
class NewVideoForm(forms.Form):
    title = forms.CharField(label='Title', max_length=700)
    description = forms.CharField(label='Description', max_length=300)
    file = forms.FileField()
