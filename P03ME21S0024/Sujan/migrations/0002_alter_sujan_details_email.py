# Generated by Django 4.0.6 on 2022-08-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sujan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sujan_details',
            name='email',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
    ]
