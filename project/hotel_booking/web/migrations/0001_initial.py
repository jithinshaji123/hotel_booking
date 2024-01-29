# Generated by Django 5.0.1 on 2024-01-08 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=220)),
                ('Email', models.EmailField(max_length=220)),
                ('Password', models.CharField(max_length=8)),
                ('Confirm_password', models.CharField(max_length=8)),
            ],
        ),
    ]