# Generated by Django 2.0.1 on 2008-01-01 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campusbuy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemadvert',
            name='Asking_Price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='itemadvert',
            name='Description',
            field=models.TextField(max_length=100),
        ),
    ]