# Generated by Django 4.1.4 on 2023-01-02 17:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reel',
            old_name='image',
            new_name='picture',
        ),
        migrations.AlterField(
            model_name='message',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='chat.group'),
        ),
        migrations.AlterField(
            model_name='message',
            name='reciever',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='recieved_messages', to=settings.AUTH_USER_MODEL),
        ),
    ]
