# Generated by Django 4.1.5 on 2023-06-02 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='account_database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('credit_debit', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=100)),
                ('account', models.CharField(max_length=100)),
                ('particular', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('notes', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='balance_sheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rs2000', models.IntegerField()),
                ('rs500', models.IntegerField()),
                ('rs200', models.IntegerField()),
                ('rs100', models.IntegerField()),
                ('rs50', models.IntegerField()),
                ('rs20', models.IntegerField()),
                ('rs10', models.IntegerField()),
                ('rs5', models.IntegerField()),
                ('rs2', models.IntegerField()),
                ('rs1', models.IntegerField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='category_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('category_names', models.CharField(max_length=100)),
            ],
        ),
    ]
