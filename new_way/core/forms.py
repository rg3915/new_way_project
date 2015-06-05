from django import forms
from .models import Customer, Ordered
from .lists import gender_list, uf_list


class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(
        label='Sexo', choices=gender_list, initial='M', widget=forms.RadioSelect)

    class Meta:
        model = Customer
        fields = '__all__'


class OrderedForm(forms.ModelForm):

    class Meta:
        model = Ordered
        fields = '__all__'
