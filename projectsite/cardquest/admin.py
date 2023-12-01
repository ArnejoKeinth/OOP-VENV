from django.contrib import admin
from.models import PokemonCard
from.models import Trainer

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "birthdate", "location", "email")
    search_fields = ("name", "location",)

admin.site.register(PokemonCard)