# Generated by Django 4.0.4 on 2022-08-25 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_administrador_options_professor'),
        ('aula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AulaDoAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presenca', models.BooleanField(blank=True, default=True, null=True, verbose_name='Presença')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.aluno')),
                ('aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula.aula')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
    ]
