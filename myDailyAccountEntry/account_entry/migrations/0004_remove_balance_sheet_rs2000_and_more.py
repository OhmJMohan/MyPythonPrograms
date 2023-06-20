# Generated by Django 4.1.5 on 2023-06-20 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_entry', '0003_alter_account_database_account_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance_sheet',
            name='rs2000',
        ),
        migrations.AddField(
            model_name='balance_sheet',
            name='balance_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='balance_sheet',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='balance_sheet',
            name='status',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
