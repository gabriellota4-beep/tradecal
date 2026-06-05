from django.shortcuts import render, get_object_or_404, redirect
from .models import Trade


def home(request):
    trades = Trade.objects.all()

    return render(
        request,
        'trades/home.html',
        {'trades': trades}
    )


def delete_trade(request, trade_id):
    trade = get_object_or_404(Trade, id=trade_id)
    trade.delete()
    return redirect('home')