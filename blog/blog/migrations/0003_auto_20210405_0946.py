# Generated by Django 3.1.7 on 2021-04-05 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210405_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=200, verbose_name='توضیحات دسته بندی'),
        ),
    ]