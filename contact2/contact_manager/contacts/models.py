from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'input-field'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input-field'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'input-field'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'input-field textarea'}))
