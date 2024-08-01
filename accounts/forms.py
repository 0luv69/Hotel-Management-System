from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from . models import User, Owner, Client,Profile


# class ClientRegisterForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self, *args, **kwargs):
#         user = super().save(commit=False)
#         user.is_client = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.email = self.cleaned_data.get('email')
#         user.save()
#         client = Client.objects.create(user=user)
#         client.save()
#         return user


# class OwnerRegisterForm(UserCreationForm):
#     first_name = forms.CharField(required=True)
#     last_name = forms.CharField(required=True)
#     email = forms.EmailField(required=True)

#     class Meta(UserCreationForm.Meta):
#         model = User

#     @transaction.atomic
#     def save(self, *args, **kwargs):
#         user = super().save(commit=False)
#         user.is_owner = True
#         user.first_name = self.cleaned_data.get('first_name')
#         user.last_name = self.cleaned_data.get('last_name')
#         user.email = self.cleaned_data.get('email')
#         user.save()
#         owner = Owner.objects.create(user=user)
#         owner.save()
#         return user
  
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    is_owner = forms.BooleanField(required=False, label='Register as Owner')
    

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        if self.cleaned_data.get('is_owner'):
            user.is_owner = True
        else:
            user.is_client = True

        user.save()

        if user.is_owner:
            Owner.objects.create(user=user)
        else:
            Client.objects.create(user=user)

        return user
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] 

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio' ,'address', 'location']     