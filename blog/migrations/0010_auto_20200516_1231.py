# Generated by Django 3.0.6 on 2020-05-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0009_auto_20200216_1243"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="slug",
            field=models.CharField(max_length=250, null=True),
        ),
    ]
