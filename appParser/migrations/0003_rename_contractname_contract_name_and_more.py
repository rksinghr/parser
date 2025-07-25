# Generated by Django 5.2.1 on 2025-06-04 10:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appParser', '0002_rename_created_at_configrec_createdat_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract',
            old_name='contractName',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='parser',
        ),
        migrations.AddField(
            model_name='contract',
            name='frequency',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='appParser.frequency'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='fullName',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='outputObjectName',
            field=models.CharField(default='s', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='outputSchemaName',
            field=models.CharField(default='s', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='preProcessor',
            field=models.CharField(default='s', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contract',
            name='sourceFileNamingConvention',
            field=models.CharField(default='s', max_length=1000),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ConfigLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logId', models.CharField(max_length=50)),
                ('isActive', models.BooleanField(default=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('parser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appParser.parser')),
            ],
        ),
    ]
