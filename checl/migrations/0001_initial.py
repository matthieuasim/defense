# Generated by Django 4.2.2 on 2023-08-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ville', models.CharField(choices=[('Kinshasa', 'Kinshasa'), ('Lubumbashi', 'Lubumbashi'), ('Goma', 'Goma'), ('Bunia', 'Bunia'), ('Bukavu', 'Bukavu'), ('Isiro', 'Isiro'), ('Buta', 'Buta'), ('Butembo', 'Butembo')], max_length=200, null=True)),
                ('gender', models.CharField(choices=[('Feminin', 'Feminin'), ('Masculin', 'Masculin')], max_length=200, null=True)),
                ('assertion1', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=200, null=True)),
                ('assertion2', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON'), ('Peut être', 'peut')], max_length=200, null=True)),
                ('assertion3', models.CharField(choices=[('La gestion de déchets dans notre ville est inefficace et insuffisante ce qui entraine une pollution visuelle, olfactive et sanitaire des routes et des marchés', 'a'), ('La gestion de déchets dans notre ville est participative et responsable, ce qui favorise la sensibilisation, la réduction et le recyclage de déchets par les habitants, les commerçants et les autorités', 'b'), ('La gestion de déchets dans notre ville est variable selon les quartiers, les types de déchets et les acteurs impliques, ce qui crée des inégalités et des contrastes entre les routes et les marchés', 'c')], max_length=350, null=True)),
                ('assertion4', models.CharField(choices=[('C’est une bonne idée, car cela pourrait aider à adapter la fréquence et le volume de collecte en fonction du niveau de remplissage et de la décomposition de déchets, et ainsi éviter le débordement, les nuisances olfactives et les risques sanitaire', 'a'), ('Je pense que c’est une solution innovante, car cela permettrait de collecter plus efficacement les déchets, d’améliorer leur qualité et leur traçabilité, et de renforcer la sensibilisation des citoyens au tri sélectif', 'b'), ('Je crois que ce pas une bonne idée', 'c')], max_length=350, null=True)),
                ('assertion5', models.CharField(choices=[('OUI', 'OUI'), ('NON', 'NON')], max_length=350, null=True)),
                ('assertion6', models.CharField(choices=[('Environs une heure', 'a'), ('Une demi-journée', 'b'), ('Une journée', 'c'), ('Plusieurs jours et de temps en temps', 'd')], max_length=350, null=True)),
                ('assertion7', models.CharField(choices=[('Robinet public', 'a'), ('Puits privé', 'b'), ('Puits communautaire', 'c'), ('Forage', 'd'), ('Eau de pluie', 'e'), ('Autre', 'f')], max_length=350, null=True)),
                ('assertion8', models.CharField(choices=[('Oui', 'OUI'), ('Non', 'NON')], max_length=350, null=True)),
                ('assertion9', models.CharField(choices=[('Excellent', 'a'), ('Moyen', 'b'), ('Nul', 'c')], max_length=350, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'candidates',
            },
        ),
    ]
