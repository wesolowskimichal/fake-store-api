# Generated by Django 5.0.6 on 2024-06-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_user_last_name_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default='Unknown', help_text='Required. Last name', max_length=150),
            preserve_default=False,
        ),
    ]
