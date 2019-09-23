# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-11 10:38
from __future__ import unicode_literals

from django.db import migrations
from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission


def create_default_permissions_group(apps, schema_editor):
    '''
    Create the 'mydata-default-permissions' group
    '''
    # First, we need to ensure that permissions have been created,
    # then we can create a group and assign those permissions to it:
    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, apps=apps, verbosity=0)
        app_config.models_module = None

    group = Group.objects.create(name='mydata-default-permissions')
    tardis_portal_app_permissions = [
        'add_instrument', 'change_instrument', 'add_experiment',
        'change_experiment', 'add_experimentparameterset', 'add_objectacl',
        'add_dataset', 'change_dataset', 'add_datafile']
    for perm in tardis_portal_app_permissions:
        group.permissions.add(
            Permission.objects.get(
                codename=perm, content_type__app_label='tardis_portal'))
    mydata_app_permissions = [
        'add_uploader', 'change_uploader',
        'add_uploaderregistrationrequest', 'change_uploaderregistrationrequest',
        'add_uploadersetting', 'change_uploadersetting']
    for perm in mydata_app_permissions:
        group.permissions.add(
            Permission.objects.get(
                codename=perm, content_type__app_label='mydata'))


class Migration(migrations.Migration):

    dependencies = [
        ('mydata', '0003_uploadersetting_blank'),
        ('auth', '0008_alter_user_username_max_length')
    ]

    operations = [
        migrations.RunPython(create_default_permissions_group)
    ]