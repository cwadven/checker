# Generated by Django 4.1.10 on 2024-08-09 13:28
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_alter_map_options'),
        ('member', '0003_create_admin_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberMapSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='map.map')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '회원 맵 구독',
                'verbose_name_plural': '회원 맵 구독',
            },
        ),
    ]