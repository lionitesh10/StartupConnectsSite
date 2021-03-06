# Generated by Django 3.2.8 on 2021-11-05 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StartupsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startupname', models.CharField(max_length=256)),
                ('category', models.CharField(choices=[('T', 'Tech'), ('A', 'Agricultural'), ('E', 'ECommerce'), ('M', 'Medical'), ('O', 'Others')], max_length=1)),
                ('description', models.TextField()),
                ('vision', models.TextField()),
                ('startedDate', models.DateTimeField()),
                ('location', models.CharField(max_length=256)),
                ('phone_number', models.CharField(max_length=20)),
                ('phone_number2', models.CharField(max_length=20)),
                ('Datetime', models.DateTimeField(auto_now=True)),
                ('problem', models.TextField()),
                ('logo', models.CharField(max_length=256)),
                ('banner', models.CharField(blank=True, max_length=256, null=True)),
                ('primary_color', models.CharField(max_length=50)),
                ('secondary_color', models.CharField(blank=True, max_length=50, null=True)),
                ('startup_quote', models.CharField(blank=True, max_length=555)),
                ('is_verified', models.BooleanField(default=False)),
                ('ceo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='members.ceos')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startups.startupsinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
