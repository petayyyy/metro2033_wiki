from django.urls import path
from . import views

urlpatterns = [
    path('factions/', views.FactionListView.as_view(), name='faction_list'),
    path('factions/<int:pk>/', views.FactionDetailView.as_view(), name='faction_detail'),
    path('characters/', views.CharacterListView.as_view(), name='character_list'),
    path('characters/<int:pk>/', views.CharacterDetailView.as_view(), name='character_detail'),
    path('metros/', views.MetroListView.as_view(), name='metro_list'),
    path('metros/<int:pk>/', views.MetroDetailView.as_view(), name='metro_detail'),
    path('', views.HomePageView.as_view(), name='base'),
    path('admin', views.AdminPageView.as_view(), name='admin'),
]