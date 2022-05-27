from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

<<<<<<< HEAD
from accounts.models import UserProfile

=======
>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)

class editProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


<<<<<<< HEAD
class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('username', 'first_name', 'last_name', 'email', 'profile_pic')
=======
# class ProfileForm(forms.ModelForm):
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

#     class Meta:
#         model = UserProfile
#         fields = ('username', 'first_name', 'last_name', 'email', 'profile_pic')
>>>>>>> 20a6a45 (Tips Authentication: Creating a user profile and connecting the tip model to it)
