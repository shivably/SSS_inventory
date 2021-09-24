from django import forms

from com.models import Customer, FeedBack


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
