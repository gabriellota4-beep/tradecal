from django.contrib import admin
from django.urls import include, path
from trades import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('add/', views.add_trade, name='add_trade'),
    path('edit/<int:trade_id>/', views.edit_trade, name='edit_trade'),
    path('delete/<int:trade_id>/', views.delete_trade, name='delete_trade'),
    path('admin/', admin.site.urls),
]
