# newsletter/forms.py

from django import forms
from .models import Subscriber

# Manual Form
class SubscriberManualForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        if Subscriber.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already subscribed.")
        return email

# ModelForm
class SubscriberModelForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Subscriber.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("This email is already subscribed.")
        return email
