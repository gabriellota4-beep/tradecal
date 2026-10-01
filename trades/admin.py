from django.contrib import admin
from .models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('instrument', 'direction', 'user', 'entry_price', 'exit_price', 'created_on')
    list_filter = ('direction', 'created_on')
    search_fields = ('instrument', 'user__username', 'notes')
