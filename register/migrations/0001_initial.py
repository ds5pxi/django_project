# Generated by Django 5.0.6 on 2024-05-28 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myweb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('아이디', models.CharField(max_length=45)),
                ('암호', models.CharField(max_length=255)),
                ('이름', models.CharField(max_length=255)),
                ('전화번호', models.CharField(max_length=255)),
                ('생년월일', models.DateTimeField()),
                ('이메일', models.CharField(max_length=255)),
            ],
        ),
    ]
