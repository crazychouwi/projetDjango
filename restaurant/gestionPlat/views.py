# -*- coding: utf-8 -*-

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# def plat(request):
    # """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # text = u""" <h1>Bienvenue dans mon Restaurant !</h1>
    #         <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    # return HttpResponse(text)
def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = u"""<h1>Bienvenue au restaurant du bord de plage !</h1>
              <p>Le restaurant ouvrira ses portes bientot !</p>"""
    return HttpResponse(text)
