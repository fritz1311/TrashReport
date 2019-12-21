# -*- coding:utf-8 -*-

from django import forms

class ConnectForm(forms.Form):
    """gere le formulaire de connexion"""
    pseudo = forms.CharField(label="pseudo", max_length = 20)
    password = forms.CharField(widget = forms.PasswordInput)