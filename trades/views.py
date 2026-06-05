from django.shortcuts import render, get_object_or_404, redirect
from .models import Trade
from .forms import TradeForm


def home(request):
    trades = Trade.objects.all()

    return render(
        request,
        'trades/home.html',
        {'trades': trades}
    )


def add_trade(request):
    if request.method == 'POST':
        form = TradeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = TradeForm()

    return render(
        request,
        'trades/add_trade.html',
        {'form': form}
    )


def delete_trade(request, trade_id):
    trade = get_object_or_404(Trade, id=trade_id)
    trade.delete()
    return redirect('home')