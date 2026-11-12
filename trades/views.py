from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import SignUpForm, TradeForm
from .models import Trade


def home(request):
    trades = Trade.objects.filter(user=request.user) if request.user.is_authenticated else Trade.objects.none()
    return render(request, 'trades/home.html', {'trades': trades})


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created. Welcome to TradCal.')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def add_trade(request):
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.user = request.user
            trade.save()
            messages.success(request, 'Trade added successfully.')
            return redirect('home')
    else:
        form = TradeForm()
    return render(request, 'trades/trade_form.html', {'form': form, 'title': 'Add Trade', 'button_text': 'Save Trade'})


@login_required
def edit_trade(request, trade_id):
    trade = get_object_or_404(Trade, id=trade_id, user=request.user)
    if request.method == 'POST':
        form = TradeForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Trade updated successfully.')
            return redirect('home')
    else:
        form = TradeForm(instance=trade)
    return render(request, 'trades/trade_form.html', {'form': form, 'title': 'Edit Trade', 'button_text': 'Update Trade'})


@login_required
@require_POST
def delete_trade(request, trade_id):
    trade = get_object_or_404(Trade, id=trade_id, user=request.user)
    trade.delete()
    messages.success(request, 'Trade deleted successfully.')
    return redirect('home')
