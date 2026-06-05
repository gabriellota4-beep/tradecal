from django.contrib import admin
from django.urls import path
from trades import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_trade, name='add_trade'),
    path('delete/<int:trade_id>/', views.delete_trade, name='delete_trade'),
    path('admin/', admin.site.urls),
]