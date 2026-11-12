from decimal import Decimal
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import Trade


class TradeCrudTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='trader', password='strong-pass-123')
        self.other = User.objects.create_user(username='other', password='strong-pass-123')
        self.trade = Trade.objects.create(
            user=self.user, instrument='MNQ', direction='Long',
            entry_price=Decimal('20000.00'), exit_price=Decimal('20050.00'), notes='CODE4 test'
        )

    def test_home_requires_login_to_show_trades(self):
        response = self.client.get(reverse('home'))
        self.assertNotContains(response, 'CODE4 test')

    def test_user_can_create_trade(self):
        self.client.login(username='trader', password='strong-pass-123')
        response = self.client.post(reverse('add_trade'), {
            'instrument': 'NQ', 'direction': 'Short', 'entry_price': '20100',
            'exit_price': '20050', 'notes': 'New trade'
        })
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(Trade.objects.filter(user=self.user, instrument='NQ').exists())

    def test_user_can_update_own_trade(self):
        self.client.login(username='trader', password='strong-pass-123')
        response = self.client.post(reverse('edit_trade', args=[self.trade.id]), {
            'instrument': 'MNQ', 'direction': 'Long', 'entry_price': '20000',
            'exit_price': '20100', 'notes': 'Updated'
        })
        self.assertRedirects(response, reverse('home'))
        self.trade.refresh_from_db()
        self.assertEqual(self.trade.notes, 'Updated')

    def test_user_cannot_edit_another_users_trade(self):
        self.client.login(username='other', password='strong-pass-123')
        response = self.client.get(reverse('edit_trade', args=[self.trade.id]))
        self.assertEqual(response.status_code, 404)

    def test_delete_requires_post_and_ownership(self):
        self.client.login(username='trader', password='strong-pass-123')
        get_response = self.client.get(reverse('delete_trade', args=[self.trade.id]))
        self.assertEqual(get_response.status_code, 405)
        self.client.post(reverse('delete_trade', args=[self.trade.id]))
        self.assertFalse(Trade.objects.filter(id=self.trade.id).exists())
