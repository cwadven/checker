# Generated by Django 4.1.10 on 2024-08-04 11:22
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
        ('network', '0001_initial'),
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
        migrations.CreateModel(
            name='MemberNodeAcquisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acquisition_pk', models.CharField(blank=True, db_index=True, max_length=256, null=True)),
                ('acquisition_pk_type', models.CharField(choices=[('START_NODE', 'START_NODE'), ('NODE_ACQUISITION_RULE', 'NODE_ACQUISITION_RULE')], max_length=256)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='map.map')),
                ('member_map_subscription', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.membermapsubscription')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='network.node')),
            ],
            options={
                'verbose_name': '회원 노드 획득',
                'verbose_name_plural': '회원 노드 획득',
            },
        ),
        migrations.CreateModel(
            name='MemberArrowAcquisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('arrow', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='network.arrow')),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='map.map')),
                ('member_map_subscription', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.membermapsubscription')),
            ],
            options={
                'verbose_name': '회원 화살 획득',
                'verbose_name_plural': '회원 화살 획득',
            },
        ),
    ]