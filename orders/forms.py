from django import forms
from .models import *

class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
class CartForm(forms.Form):
    # name = forms.CharField(required=True)
    # phone = forms.CharField(required=True)
    nmb = forms.CharField(required=True)
