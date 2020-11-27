# Generated by Django 3.1.2 on 2020-11-27 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('includeFrame', models.BooleanField()),
                ('side', models.CharField(choices=[('L', 'Left'), ('R', 'Right'), ('B', 'Both')], max_length=1)),
                ('magnification', models.CharField(choices=[('F', 'Far'), ('C', 'Close')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(null=True)),
                ('lens', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.lens')),
            ],
        ),
    ]