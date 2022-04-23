# Generated by Django 4.0.4 on 2022-04-23 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assunto', models.CharField(max_length=50, verbose_name='Assunto da aula')),
                ('datetime', models.DateTimeField()),
                ('idArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.area')),
                ('idProfessor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.professor')),
            ],
            options={
                'ordering': ('-datetime',),
            },
        ),
        migrations.CreateModel(
            name='AulaDoAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idAluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.aluno')),
                ('idAula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula.aula')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
