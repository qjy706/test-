# Generated by Django 2.1.7 on 2019-03-18 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20190317_0808'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teachers',
            options={'verbose_name': '老师', 'verbose_name_plural': '老师'},
        ),
        migrations.AlterField(
            model_name='teachers',
            name='age',
            field=models.IntegerField(max_length=20, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='name',
            field=models.CharField(max_length=20, verbose_name='老师'),
        ),
        migrations.AlterModelTable(
            name='teachers',
            table='Teachers',
        ),
    ]
