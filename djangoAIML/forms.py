from django import forms

class SymptomForm(forms.Form):
    text = forms.CharField(
        label = "Describe your symptoms",
        widget = forms.Textarea,
        required = True
    )