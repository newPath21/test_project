# Generated by Django 3.0.14 on 2022-06-30 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0002_auto_20220630_0436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggeditem',
            name='content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]
