# Generated by Django 3.0.5 on 2020-04-08 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categoria',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Curso',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('matricula', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Professor',
            },
        ),
        migrations.CreateModel(
            name='Trabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('descricao', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('date', models.DateField(auto_now=True, verbose_name='Date de Cadastro')),
                ('ano', models.IntegerField()),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.Categoria', verbose_name='Categoria')),
                ('curso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='principal.Curso', verbose_name='Curso')),
                ('professores', models.ManyToManyField(to='principal.Professor')),
            ],
        ),
    ]
