# Generated by Django 2.0.7 on 2019-05-28 09:40
from sys import _getframe

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid

from ...common.setup_utils import NotConfiguredException, validate_attr


def init_manager_group(apps, schema_editor):
    validate_attr(_getframe().f_code.co_filename, _getframe().f_code.co_name, _getframe().f_lineno, 'TESTING')

    if not settings.TESTING:
        Group = apps.get_model('oneid_meta', 'Group')
        root = Group.objects.get(uid='root')
        manager = Group.objects.filter(uid='manager').first()
        if not manager:
            manager = Group.objects.create(uid='manager', name='管理员', parent=root)

class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0025_register_apps'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('depts', jsonfield.fields.JSONField(blank=True, default=[], verbose_name='部门uids')),
                ('dept_subject', models.CharField(choices=[('tree', '自动涵盖指定部门及下级部门'), ('node', '指定部门'), ('self_node', '所在部门'), ('self_tree', '自动涵盖所在部门及下级部门')], default='tree', max_length=128, verbose_name='部门范围类型')),
                ('apps', jsonfield.fields.JSONField(blank=True, default=[], verbose_name='应用uid')),
                ('all_apps', models.BooleanField(default=False, verbose_name='全部应用权限')),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='oneid_meta.Group', verbose_name='Group')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(init_manager_group),
    ]
