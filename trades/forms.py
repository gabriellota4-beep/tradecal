from django import forms
from .models import Trade


class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = [
            'instrument',
            'direction',
            'entry_price',
            'exit_price',
            'notes'
        ]