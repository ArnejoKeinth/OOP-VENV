from django.contrib import admin
from .models import PokemonCard, Trainer

@admin.register(PokemonCard)
class PokemonCardAdmin(admin.ModelAdmin):
    list_display = ("name", "rarity")
    search_fields = ("name",)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "location", "email")
    search_fields = ("name", "location",)
