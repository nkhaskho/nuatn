# Generated by Django 3.2.9 on 2021-11-04 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('gps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gps',
            old_name='timestamp',
            new_name='created_at',
        ),
        migrations.CreateModel(
            name='GPSCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='other', to='users.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]