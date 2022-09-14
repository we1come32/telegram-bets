# Generated by Django 4.1.1 on 2022-09-14 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Data', '0001_initial'),
        ('AUTH', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiBet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('value', models.FloatField()),
                ('canceled', models.BooleanField(default=False)),
                ('payed', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AUTH.account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SingleBet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
                ('value', models.FloatField()),
                ('canceled', models.BooleanField(default=False)),
                ('payed', models.BooleanField(default=False)),
                ('multi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bets.multibet', verbose_name='bets')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data.eventteam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AUTH.account')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]