# Generated by Django 4.2.7 on 2024-03-25 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_categoria_produto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
