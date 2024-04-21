from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    AUTEUR = 'AUTEUR'
    UTILISATEUR = 'UTILISATEUR'

    CHOIX_ROLE = (
        (AUTEUR, 'Auteur'),
        (UTILISATEUR, 'Utilisateur')
        )

    profile_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=CHOIX_ROLE)
