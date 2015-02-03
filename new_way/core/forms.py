from django import forms
from .models import UserProfile, Person, Customer, Employee, Occupation, Dealership


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'


class CustomerForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
