# Generated by Django 4.2.13 on 2024-06-22 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_member_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
