# Generated by Django 2.0.7 on 2019-07-25 07:37

from django.db import migrations, models
from django.conf import settings
import django.db.models.deletion
from sys import _getframe
from ...common.setup_utils import validate_attr
from ...oneid_meta.models import config
import uuid


def init_email_config(apps, schema_editor):

    EmailConfig = apps.get_model('oneid_meta', 'EmailConfig')
    Site = apps.get_model('sites', 'Site')
    validate_attr(_getframe().f_code.co_filename, _getframe().f_code.co_name, _getframe().f_lineno,
                  'SITE_ID')
    site, _ = Site.objects.get_or_create(id=settings.SITE_ID)
    EmailConfig.objects.get_or_create(site=site)


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('oneid_meta', '0045_add_building_perm'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('host', models.CharField(blank=True, default='', max_length=256, verbose_name='邮件服务地址')),
                ('port', models.IntegerField(blank=True, default=587, verbose_name='邮件服务端口')),
                ('access_key', models.CharField(blank=True, default='', max_length=512, verbose_name='邮箱账号')),
                ('access_secret', models.CharField(blank=True, default='', max_length=512, verbose_name='邮箱密钥')),
                ('nickname', models.CharField(blank=True, default='OneID', max_length=128, verbose_name='邮件发送人落款')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='email_config', to='sites.Site')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, config.SingletonConfigMixin),
        ),
        migrations.RunPython(init_email_config)
    ]
