# Generated by Django 4.2 on 2023-07-10 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Peixes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=30)),
                ('pesoMedioPeixe_kg', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Piscicultores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('piscicultor', models.CharField(max_length=30)),
                ('rg', models.CharField(max_length=7)),
                ('contato', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Racao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidaderacaokg', models.CharField(max_length=30)),
                ('marcaracao', models.CharField(max_length=30)),
                ('precoracao', models.CharField(max_length=30)),
                ('protreinabruta', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Viveiros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biomassaViveiro', models.CharField(max_length=30)),
                ('dataIniciar', models.CharField(max_length=30)),
                ('mortalidade', models.CharField(max_length=30)),
                ('dataRetirada', models.CharField(max_length=30)),
                ('numeroViveiro', models.IntegerField()),
                ('temperatura', models.CharField(max_length=30)),
                ('largura_M', models.CharField(max_length=30)),
                ('ganhoViveiro', models.CharField(max_length=30)),
                ('ladoMenor_M', models.CharField(max_length=30)),
                ('pH_daAgua', models.CharField(max_length=30)),
                ('amostragemViveiro', models.CharField(max_length=30)),
                ('numeroPeixesViveiro', models.IntegerField()),
                ('Piscicultores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.piscicultores')),
            ],
        ),
    ]