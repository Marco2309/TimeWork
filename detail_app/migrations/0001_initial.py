# Generated by Django 3.2.3 on 2021-05-25 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice', models.IntegerField()),
                ('type', models.CharField(max_length=10)),
                ('date_time', models.CharField(max_length=200)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateField(auto_now_add=True)),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='detail', to='task_app.task')),
            ],
        ),
    ]
