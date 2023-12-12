from django.contrib import admin
from .models import Trainer, PokemonCard, Collection

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email')
    search_fields = ('name', 'location')

@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):  # Fix the class name here
    list_display = ('name', 'rarity')
    search_fields = ('name',)

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('trainer', 'card', 'collection_date')
    search_fields = ('trainer__name', 'card__name')
