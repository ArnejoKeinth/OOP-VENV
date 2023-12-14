from django.urls import path
from . import views
from .views import HomePageView, TrainerList, PokemonCardList, CollectionList

urlpatterns = [
    # Home
    path('', views.HomePageView.as_view(), name='home'),

    # Trainers
    path('trainer_list', views.TrainerList.as_view(), name='trainer-list'),
    path('trainer_list/add', views.TrainerCreateView.as_view(), name='trainer-add'),
    path('trainer_list/<pk>', views.TrainerUpdateView.as_view(), name='trainer-update'),
    path('trainer_list/<pk>/delete', views.TrainerDeleteView.as_view(), name='trainer-delete'),

    # Pokemons
    path('pokemon_card', views.PokemonCardList.as_view(), name='pokemon-card'),
    path('pokemon_card/add', views.PokemonCardCreateView.as_view(), name='pokemon-card-add'),
    path('pokemon_card/<pk>', views.PokemonCardUpdateView.as_view(), name='pokemon-card-update'),
    path('pokemon_card/<pk>/delete', views.PokemonCardDeleteView.as_view(), name='pokemon-card-delete'),

    # Collections
    path('collection_list', views.CollectionList.as_view(), name='collection-list'),
    path('collection_list/add', views.CollectionCreateView.as_view(), name='collection-list-add'),
    path('collection_list/<pk>', views.CollectionUpdateView.as_view(), name='collection-list-update'),
    path('collection_list/<pk>/delete', views.CollectionDeleteView.as_view(), name='collection-list-delete'),
]