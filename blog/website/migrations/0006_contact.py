# Generated by Django 3.2.5 on 2021-08-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_post_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
