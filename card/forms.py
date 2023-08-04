from django import forms

PRODUCT_QUANTITY_CHOISES=[(i,str(i))for i in range(1,100)]

class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOISES , coerce=int)
    update=forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
