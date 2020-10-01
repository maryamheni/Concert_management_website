# Generated by Django 3.1.1 on 2020-09-28 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=20)),
                ('country', models.CharField(choices=[('tunisia', 'Tunisia'), ('usa', 'Usa')], max_length=20)),
            ],
        ),
    ]