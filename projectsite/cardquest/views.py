from django.shortcuts import render
from typing import Any
from django.views.generic.list import ListView
from .models import PokemonCard, Trainer, Collection
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import TrainerForm, PokemonCardForm, CollectionForm
from django.urls import reverse_lazy

class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "home.html"
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 15

class TrainerCreateView(CreateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_add.html'
    success_url = reverse_lazy('trainer-list')

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'trainer_edit.html'
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')

class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon-card'
    template_name = 'pokemon-card.html'
    paginate_by = 15


class PokemonCardCreateView(CreateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_card_add.html'
    success_url = reverse_lazy('pokemon-card')


class PokemonCardUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_card_edit.html'
    success_url = reverse_lazy('pokemon-card')


class PokemonCardDeleteView(DeleteView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'pokemon_card_del.html'
    success_url = reverse_lazy('pokemon-card')


class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 15


class CollectionCreateView(CreateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections_add.html'
    success_url = reverse_lazy('collection-list')


class CollectionUpdateView(UpdateView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections_edit.html'
    success_url = reverse_lazy('collection-list')


class CollectionDeleteView(DeleteView):
    model = Collection
    form_class = CollectionForm
    template_name = 'collections_del.html'
    success_url = reverse_lazy('collection-list')