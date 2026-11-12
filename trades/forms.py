from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Trade


class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['instrument', 'direction', 'entry_price', 'exit_price', 'notes']
        widgets = {
            'instrument': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. MNQ'}),
            'direction': forms.Select(attrs={'class': 'form-select'}),
            'entry_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'exit_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Setup, execution and lessons...'}),
        }

    def clean(self):
        cleaned = super().clean()
        entry = cleaned.get('entry_price')
        exit_price = cleaned.get('exit_price')
        if entry is not None and entry <= 0:
            self.add_error('entry_price', 'Entry price must be greater than zero.')
        if exit_price is not None and exit_price <= 0:
            self.add_error('exit_price', 'Exit price must be greater than zero.')
        return cleaned


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')
