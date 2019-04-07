from django import forms
from django.contrib.auth import get_user_model
User=get_user_model()


class ContactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"fullname","placeholder":"your full name"}))
    email    = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control","id":"fullname","placeholder":"your email"}))
    content  = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","id":"textarea","placeholder":"your message"}))


    def clean_email(self):
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("email has to be gmail.com")
        return email

class RegisterForm(forms.Form):

    username = forms.CharField(label='Your name',widget=forms.TextInput(attrs={ "class":"form-control","placeholder":"Enter username" ,"name": "username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder": "Enter email", "name": "email"}))
    password = forms.CharField(label='Enter password',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "Enter password","name" :"password1" }))
    password2 = forms.CharField(label='Retype Password',widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "Enter password","name" :"password2"}))

    # Username = forms.CharField()
    # email = forms.CharField()
    # password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Retype Password', widget=forms.PasswordInput)

    def clean_email(self):
        email=self.cleaned_data.get("email")
        email = User.objects.filter(email=email)
        if email.exists():
            raise forms.ValidationError("username taken")
        return email



    # def clean_email(self):
    #     email=self.cleaned_data.get("Email")
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("email has to be gmail.com")
    #     return email

    def clean_password(self):
        data=self.cleaned_data
        password1=self.cleaned_data.get("password")
        password2 =self.cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("password is not matched")
        return data

    # def clean_email(self):
    #     email=self.cleaned_data.get("email")
    #
    #     data = self.cleaned_data
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #
    #     if password1 != password2:
    #         raise forms.ValidationError("password is not matched")
    #
    #
    #     if not "gmail.com" in email:
    #         raise forms.ValidationError("email has to be gmail.com")
    #     return data

    def clean_username(self):

        user =  self.cleaned_data.get("username")
        user=User.objects.filter(username=user)
        if user.exists():
            raise forms.ValidationError("username taken")
        return user










