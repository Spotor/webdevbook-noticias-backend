# Generated by Django 2.1.2 on 2018-10-15 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('resumo', models.TextField()),
                ('conteudo', models.TextField(verbose_name='conteúdo')),
                ('data', models.DateTimeField(auto_now=True)),
                ('destaque', models.BooleanField(default=False)),
                ('fotoUrl', models.URLField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nb_back.Pessoa'),
        ),
    ]