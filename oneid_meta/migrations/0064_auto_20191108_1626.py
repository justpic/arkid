# Generated by Django 2.0.13 on 2019-11-08 08:26
from sys import _getframe

from django.db import migrations, models
from django.conf import settings

from ...common.setup_utils import NotConfiguredException, validate_attr


def rename_root_dept(apps, schema_editor):
    '''
    将 root dept 重命名为 `部门`
    '''
    Dept = apps.get_model('oneid_meta', 'Dept')

    root_dept, _ = Dept.objects.get_or_create(uid='root', is_del=False)
    root_dept.name = '部门'
    root_dept.save()

class Migration(migrations.Migration):

    dependencies = [
        ('oneid_meta', '0063_auto_20191104_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='require_reset_password',
            field=models.BooleanField(default=False, verbose_name='是否需要重置密码'),
        ),
        migrations.AlterField(
            model_name='emailconfig',
            name='nickname',
            field=models.CharField(blank=True, default='ArkID', max_length=128, verbose_name='邮件发送人落款'),
        ),
    ]

    validate_attr(_getframe().f_code.co_filename, _getframe().f_code.co_name, _getframe().f_lineno, 'TESTING')

    if not settings.TESTING:
        operations += [
            migrations.RunPython(rename_root_dept),
        ]
