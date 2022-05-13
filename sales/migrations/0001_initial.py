# Generated by Django 4.0.4 on 2022-05-12 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('stock_name', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('sales_id', models.CharField(max_length=20)),
                ('customer_id', models.CharField(max_length=20)),
                ('manager_id', models.CharField(max_length=20)),
            ],
        ),
    ]