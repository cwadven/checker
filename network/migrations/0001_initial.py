# Generated by Django 4.1.10 on 2024-08-04 11:21
import django.contrib.postgres.indexes
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('map', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Arrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simple_word', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('is_acquisition_only_show_info', models.BooleanField(default=False)),
                ('total_acquisition_count', models.BigIntegerField(db_index=True, default=0, help_text='총 획득 수')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simple_word', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('is_acquisition_only_show_info', models.BooleanField(default=False)),
                ('phase', models.CharField(choices=[('START', '시작'), ('END', '종료')], max_length=20, null=True)),
                ('size', models.FloatField(default=1.0)),
                ('total_acquisition_count', models.BigIntegerField(db_index=True, default=0, help_text='총 획득 수')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='map.map')),
            ],
        ),
        migrations.CreateModel(
            name='NodeAcquisitionRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=256, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('arrows', models.ManyToManyField(blank=True, help_text='노드 획득을 위한 필요한 획득 Arrow', null=True, to='network.arrow')),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='network.node')),
            ],
        ),
        migrations.CreateModel(
            name='ArrowAcquisitionRule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('arrow', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='network.arrow')),
            ],
        ),
        migrations.AddField(
            model_name='arrow',
            name='source_node',
            field=models.ForeignKey(help_text='출발지 노드', on_delete=django.db.models.deletion.DO_NOTHING, related_name='source_arrows', to='network.node'),
        ),
        migrations.AddField(
            model_name='arrow',
            name='target_node',
            field=models.ForeignKey(help_text='도착지 노드', on_delete=django.db.models.deletion.DO_NOTHING, related_name='target_arrows', to='network.node'),
        ),
        migrations.AddIndex(
            model_name='node',
            index=django.contrib.postgres.indexes.GinIndex(fields=['simple_word'], name='node_simple_word_gin_idx', opclasses=['gin_trgm_ops']),
        ),
        migrations.AddIndex(
            model_name='node',
            index=django.contrib.postgres.indexes.GinIndex(fields=['title'], name='node_title_gin_idx', opclasses=['gin_trgm_ops']),
        ),
    ]
