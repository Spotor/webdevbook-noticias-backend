# Generated by Django 2.1.2 on 2018-10-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nb_back', '0002_noticia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
