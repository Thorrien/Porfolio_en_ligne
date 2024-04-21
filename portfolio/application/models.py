from django.db import models

# Create your models here.


class Compétence(models.Model):
    def __str__(self):
        return f"{self.name} | Domaine : {self.domaine} | Etat : {self.etat}"

    class Domaine(models.TextChoices):
        AGRICULTURE_PAYSAGE = 'AGRI'
        ALIMENTATION = 'ALIM'
        ASSOCIATIF = 'ASSO'
        ANIMAUX = 'ANIM'
        ARCHITECTURE_DECORATION = 'ARCH'
        SECOURS_SECURITE = 'SECO'
        ARTISANAT_DESIGN_MODE = 'ARTI'
        BANQUE_FINANCE_ASSURANCE = 'BANQ'
        BIOLOGIE_CHIMIE = 'BIOL'
        BTP = 'BTPP'
        CINEMA = 'CINE'
        JEUX_VIDEO = 'JEUV'
        JEUX_SOCIETE = 'JEUS'
        COMMERCE_IMMOBILIER = 'COME'
        COMMUNICATION_MARKETING = 'COMU'
        CULTURE_SPECTACLE_PATRIMOINE = 'SPEC'
        DROIT_JUSTICE = 'DROIT'
        EDITION_IMPRIMERIE = 'LIVR'
        LECTURE = 'LECT'
        ELECTRONIQUE_ROBOTIQUE = 'ELEC'
        ENERGIE = 'ENER'
        ENSEIGNEMENT_FORMATION = 'FORM'
        ENVIRONNEMENT = 'ENVI'
        GESTION_ENTREPRISE = 'GEST'
        COMPTABILITE = 'COMPT'
        GESTION_RH = 'GERH'
        RESTAURATION = 'REST'
        TOURISME = 'TOUR'
        HUMANITAIRE = 'HUMA'
        INFORMATIQUE = 'INFO'
        LANGUES = 'LANG'
        INDUSTRIE = 'INDUS'
        MECANIQUE = 'MECA'
        SANTE = 'SANT'
        MATHEMATIQUES = 'MATH'
        SCIENCES_HUMAINES = 'PSYC'
        SCIENCES_PHYSIQUE = 'PHYS'
        SOCIAL = 'SOCI'
        SPORT = 'SPOR'
        TRANSPORT = 'TRANS'
        VIE = 'VIEE'

    name = models.fields.CharField(max_length=100)
    desctription = models.fields.CharField(max_length=500, null=True, blank=True)
    icone = models.ImageField()
    domaine = models.fields.CharField(choices=Domaine.choices, max_length=5)
    etat = models.fields.BooleanField(default=False)


class Defi(models.Model):
    def __str__(self):
        return f"{self.name} | Niveau : {self.niveau} | Etat : {self.etat}"

    name = models.fields.CharField(max_length=100)
    desctription = models.fields.CharField(max_length=500, null=True, blank=True)
    icone = models.ImageField()
    etat = models.fields.BooleanField(default=False)
    niveau = models.fields.IntegerField()
    compétence = models.ForeignKey(Compétence, on_delete=models.CASCADE)


class Projet(models.Model):
    def __str__(self):
        return f"{self.name} | Etat : {self.etat}"

    class Etat(models.TextChoices):
        COMPETENCES_ACQUISES = 'COM'
        MISE_EN_PLACE = 'PLA'
        EN_COURS = 'COU'
        FINALISATION = 'FIN'
        TERMINE = 'TER'

    name = models.fields.CharField(max_length=100)
    desctription = models.fields.CharField(max_length=500, null=True, blank=True)
    icone = models.ImageField()
    complexite = models.IntegerField()
    etat = models.fields.CharField(choices=Etat.choices, max_length=3)
    precisions = models.fields.CharField(max_length=500, null=True, blank=True)
    constitué = models.ManyToManyField(Compétence)
