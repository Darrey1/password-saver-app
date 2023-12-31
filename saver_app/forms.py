from django import forms
from .models import *
non_allowed_usernames = ['abc']

#The class will store all the required input fields
class RegisterForm(forms.Form):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(
        label='Password',
      #The widget handles the rendering of the HTML
        widget=forms.PasswordInput(
            attrs={
                "id": "user-password"
            }
        )
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                "id": "user-confirm-password"
            }
        )
    )
    #Check so that passwords match
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
            raise forms.ValidationError("The two passwords does not match")
        return password2

    
    def clean_username(self):
        username = self.cleaned_data.get("username")
        #The qs checks if input username matches exactly the User that is already 
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError(f"{username} doesn't match with our standard, please input another.")
        if qs.exists():
            raise forms.ValidationError(f"{username} is already in use by another user,please input another.")
            
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        #Email check
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError(f"{email} is already in use as email by another user.")
        return email



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control"
    }))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "user-password"
            }
        )
    )


    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username) # thisIsMyUsername == thisismyusername
        if not qs.exists():
            raise forms.ValidationError(f"{username} does not exist.")
        if qs.count() != 1:
            raise forms.ValidationError(f"invalid user with username {username}.")
        return username
PW_TYPES = [('confidentail', 'confidentail'),('sharable', 'sharable')]
class UserPWForm(forms.Form):
    
    title = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control"
    }))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
        "class": "form-control"
    }))
    type = forms.ChoiceField(choices=PW_TYPES, widget=forms.RadioSelect())
    

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=UserPW
        fields=['title','password', 'type']