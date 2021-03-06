# Generated by Django 3.2.6 on 2021-09-02 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(verbose_name='Texto de la pregunta')),
            ],
            options={
                'db_table': 'pregunta',
            },
        ),
        migrations.CreateModel(
            name='Opciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_correcta', models.BooleanField(default=False, verbose_name='¿Es esta la pregunta correcta?')),
                ('texto', models.TextField(verbose_name='Texto de la respuesta')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pregunta', to='preguntas.pregunta')),
            ],
            options={
                'db_table': 'opciones',
            },
        ),
    ]
