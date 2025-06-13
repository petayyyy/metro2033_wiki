from django.views.generic import ListView, DetailView
from .models import Faction, Character, Metro
from django.views.generic import TemplateView
from django.contrib import admin

class HomePageView(TemplateView):
    template_name = 'base.html'

class AdminPageView(TemplateView):
    # template_name = 'admin/'
    template_name = admin.site.urls

class FactionListView(ListView):
    model = Faction
    template_name = 'faction_list.html'

class FactionDetailView(DetailView):
    model = Faction
    template_name = 'faction_detail.html'

class CharacterListView(ListView):
    model = Character
    template_name = 'character_list.html'

class CharacterDetailView(DetailView):
    model = Character
    template_name = 'character_detail.html'

class MetroListView(ListView):
    model = Metro
    template_name = 'metro_list.html'

class MetroDetailView(DetailView):
    model = Metro
    template_name = 'metro_detail.html'