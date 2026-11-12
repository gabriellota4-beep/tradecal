from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trades', '0002_remove_trade_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trades', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trade',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='trade',
            name='direction',
            field=models.CharField(choices=[('Long', 'Long'), ('Short', 'Short')], max_length=10),
        ),
        migrations.AlterModelOptions(
            name='trade',
            options={'ordering': ['-created_on']},
        ),
    ]
