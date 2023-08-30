from django.db import models

class Candidate(models.Model):

    VILLE = (
('Kinshasa', 'Kinshasa'),
('Lubumbashi', 'Lubumbashi'),
('Goma', 'Goma'),
('Bunia', 'Bunia'),
('Bukavu', 'Bukavu'),
('Isiro', 'Isiro'),
('Buta', 'Buta'),
('Butembo', 'Butembo'),
)

    GENRE = (
        ('Feminin', 'Feminin'),
        ('Masculin', 'Masculin'),
        )
    
    
    
    ASSERSION1 = (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
    )

    ASSERSION2 = (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
        ('Peut être', 'peut'),
    )
    ASSERSION3 = (
        ("La gestion de déchets dans notre ville est inefficace et insuffisante ce qui entraine une pollution visuelle, olfactive et sanitaire des routes et des marchés", 'a'),
        ("La gestion de déchets dans notre ville est participative et responsable, ce qui favorise la sensibilisation, la réduction et le recyclage de déchets par les habitants, les commerçants et les autorités", "b"),
        ("La gestion de déchets dans notre ville est variable selon les quartiers, les types de déchets et les acteurs impliques, ce qui crée des inégalités et des contrastes entre les routes et les marchés", "c"),
    )
    ASSERSION4 = (
        ("C’est une bonne idée, car cela pourrait aider à adapter la fréquence et le volume de collecte en fonction du niveau de remplissage et de la décomposition de déchets, et ainsi éviter le débordement, les nuisances olfactives et les risques sanitaire", 'a'),
        ("Je pense que c’est une solution innovante, car cela permettrait de collecter plus efficacement les déchets, d’améliorer leur qualité et leur traçabilité, et de renforcer la sensibilisation des citoyens au tri sélectif", 'b'),
        ("Je crois que ce pas une bonne idée", 'c'),
    )
    ASSERSION5 = (
        ('OUI', 'OUI'),
        ('NON', 'NON'),
    )
    ASSERSION6 = (
        ("Environs une heure", 'a'),
        ("Une demi-journée", 'b'),
        ("Une journée", 'c'),
        ("Plusieurs jours et de temps en temps", 'd'),
    )
    ASSERSION7 = (
        ("Robinet public", 'a'),
        ("Puits privé", 'b'),
        ("Puits communautaire", 'c'),
        ("Forage", 'd'),
        ("Eau de pluie", 'e'),
        ("Autre", 'f'),
    )
    ASSERSION8 = (
        ("Oui", 'OUI'),
        ("Non", 'NON'),
    )
    ASSERSION9 = (
        ('Excellent', 'a'),
        ('Moyen', 'b'),
        ('Nul', 'c'),
    )


    name=models.CharField(max_length=100)
    ville=models.CharField(max_length=200, null=True, choices=VILLE)
    gender=models.CharField(max_length=200, null=True, choices=GENRE)
    assertion1 = models.CharField(max_length=200, null=True, choices=ASSERSION1)
    assertion2 = models.CharField(max_length=200, null=True, choices=ASSERSION2)
    assertion3 = models.CharField(max_length=350, null=True, choices=ASSERSION3)
    assertion4 = models.CharField(max_length=350, null=True, choices=ASSERSION4)
    assertion5 = models.CharField(max_length=350, null=True, choices=ASSERSION5)
    assertion6 = models.CharField(max_length=350, null=True, choices=ASSERSION6)
    assertion7 = models.CharField(max_length=350, null=True, choices=ASSERSION7)
    assertion8 = models.CharField(max_length=350, null=True, choices=ASSERSION8)
    assertion9 = models.CharField(max_length=350, null=True, choices=ASSERSION9)
    created_at = models.DateTimeField(auto_now_add=True)
   
    class Meta:
        db_table="candidates"

    def __str__(self):
        return self.name