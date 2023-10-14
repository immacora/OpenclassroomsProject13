# Generated by Django 4.2.6 on 2023-10-14 05:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('oc_lettings_site', '0002_alter_address_id_alter_letting_id_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='oc_lettings_site_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]