# Generated by Django 3.0.3 on 2020-03-04 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200302_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoloClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('total', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='dontfakeme',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
