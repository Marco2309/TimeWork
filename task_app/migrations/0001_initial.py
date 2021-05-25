# Generated by Django 3.2.3 on 2021-05-25 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=True)),
                ('repetitive', models.BooleanField(default=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]