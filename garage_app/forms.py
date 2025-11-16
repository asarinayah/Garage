from django import forms
from .models import vehicle, jobitem, invoice

class VehicleForm(forms.ModelForm):
    class Meta:
        model = vehicle
        fields = "__all__"

class JobItemForm(forms.ModelForm):
    class Meta:
        model = jobitem
        fields = "__all__"

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = invoice
        fields = ['invoice_number', 'vehicle', 'job_items', 'tax_percent', 'discount', 'paid']
        widgets = {
            'job_items': forms.CheckboxSelectMultiple()
        }
