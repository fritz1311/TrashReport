# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Listes des models du Projet CUY

class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    poste = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nom


class Agent(models.Model):
    nom = models.CharField(max_length = 255)
    poste = models.CharField(max_length=100)

    def __unicode__ (self):
        return self.nom

class Coordonnees(models.Model):
    latitude = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)

    def __unicode__(self):
        return "(",self.latitude,",",self.longitude,")"

class Bac(models.Model):
    capacite = models.IntegerField(null =  False)
    etat_remplissage = models.CharField(max_length = 255)
    frequence_remplissage = models.IntegerField(null=False)
    coordonnees = models.ForeignKey(Coordonnees, null=False)

    def __unicode__(self):
        return self.coordonnees

class Registre(models.Model):
    bac = models.ForeignKey(Bac, null=True)
    utilisateur = models.ForeignKey(Utilisateur, null=True)
    heure = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="date de modification")

    def __unicode__(self):
        return "l'utiliateur ", self.utilisateur," a entre des donnees sur le bac de coordonnees", 
        self.bac


