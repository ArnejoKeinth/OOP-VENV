from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, null=False)
    updated_at = models.DateTimeField(auto_now=True, null=False)

    class Meta:
        abstract = True

class Trainer(BaseModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    birthdate = models.DateField(null=False, blank=True, default=timezone.now)
    location = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=120, null=True, blank=True)

    def __str__(self):
        return self.name

class PokemonCard(BaseModel):
    RARITY_CHOICES = (
        ('Common', 'Common'),
        ('Uncommon', 'Uncommon'),
        ('Rare', 'Rare'),
    )

    CARDTYPE_CHOICES = (
        ('Fire', 'Fire'),
        ('Water', 'Water'),
        ('Grass', 'Grass'),
        ('Electric', 'Electric'),
        ('Psychic', 'Psychic'),
        ('Ice', 'Ice'),
        ('Dragon', 'Dragon'),
        ('Dark', 'Dark'),
        ('Normal', 'Normal'),
        ('Fighting', 'Fighting'),
        ('Flying', 'Flying'),
        ('Poison', 'Poison'),
        ('Ground', 'Ground'),
        ('Rock', 'Rock'),
        ('Bug', 'Bug'),
        ('Ghost', 'Ghost'),
        ('Steel', 'Steel'),
        ('Fairy', 'Fairy'),
    )

    name = models.CharField(max_length=100, null=True, blank=True)
    rarity = models.CharField(max_length=100, null=True, blank=True, choices=RARITY_CHOICES)
    hp = models.PositiveIntegerField(null=True, blank=True)
    card_type = models.CharField(max_length=100, null=True, blank=True, choices=CARDTYPE_CHOICES)
    attack = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    weakness = models.CharField(max_length=250, null=True, blank=True)
    card_number = models.IntegerField(null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    evolution_stage = models.CharField(max_length=250, null=True, blank=True)
    abilities = models.CharField(max_length=250, null=True, blank=True)

class Collection(BaseModel):
    name = models.CharField(max_length=255, default='Your Default Value')
    description = models.TextField(default="Default Collection Description")
    card = models.ForeignKey(PokemonCard, blank=True, null=True, on_delete=models.CASCADE, related_name='collections')
    trainer = models.ForeignKey(Trainer, blank=True, null=True, on_delete=models.CASCADE, related_name='collections')
    collection_date = models.DateTimeField(default=timezone.now)

