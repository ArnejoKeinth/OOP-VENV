from django.contrib import admin
from .models import Trainer, PokemonCard, Collection


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email', 'created_at', 'updated_at', )
    search_fields = ('name', 'location')


# Register your models here.

@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness', 'card_number', 'release_date', 'evolution_stage', 'abilities', 'created_at', 'updated_at', )
    search_fields = ('name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness', 'card_number', 'release_date', 'evolution_stage', 'abilities', )

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('card', 'trainer', 'collection_date', 'created_at', 'updated_at', )
    search_fields = ('card', 'trainer', 'collection_date', )
