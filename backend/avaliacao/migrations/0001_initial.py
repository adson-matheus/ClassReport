# Generated by Django 4.0.4 on 2022-06-22 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aula', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist', models.JSONField(verbose_name='checklist')),
                ('aula_do_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula.auladoaluno')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='AvaliacoesProfessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_avaliacao', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='avaliacao.avaliacao')),
                ('id_professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.professor')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
