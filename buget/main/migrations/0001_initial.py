# Generated by Django 3.2.5 on 2021-07-12 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyBuget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(default=0, verbose_name='total')),
                ('spent', models.IntegerField(default=0, verbose_name='spent')),
                ('actions', models.IntegerField(default=0, verbose_name='actions')),
            ],
        ),
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('comment', models.CharField(max_length=450, verbose_name='comment')),
                ('spent', models.IntegerField(verbose_name='spent money')),
                ('payed', models.BooleanField(default=False, verbose_name='payed/not payed')),
            ],
        ),
    ]