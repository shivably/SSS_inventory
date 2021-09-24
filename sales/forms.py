from django import forms

from sales.models import SalesHistory


class BillingForm(forms.ModelForm):
    class Meta:
        model = SalesHistory
        fields = "__all__"
