# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, Http404

from app.forms import ConnectForm

# Create your views here.

def connect(request):
    """gere la page de connexion utilisateur"""
    form = ConnectForm()
    #verrifiction du type denvoi de formulaire
    if request.method == 'POST':
        form = ConnectForm(request.POST or None) #nous reprenons les donnees

        if form.is_valid(): #si les donnees du formulaire sont valides

            #nous traitons les donnees du formulaire
            pseudo = form.cleaned_data['pseudo']
            password = form.cleaned_data['password']
            envoi = True
        
        else: # s'il s'agit d'une requete de type GET
            form = ConnectForm() #on cree un formulaire vide

    return render(request, 'app/connect.html', {'form': form})


def home(request):
    """page d'index du site"""

    return render(request, 'app/index.html', {})


def inscript(request):
    """page d'index du site"""

    return render(request, 'app/inscript.html', {})