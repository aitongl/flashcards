from django.contrib import admin
from django.urls import path, include
from flashcards import views

urlpatterns = [
    path('', views.allSets, name='allSets'),
    path('addSet', views.addSet, name='add_set'),
    path('viewSet/<int:id>', views.viewSet, name='view_set'),
    path('viewSet/<int:id>', views.viewSet, name='view_set'),
    path('editSet/<int:id>', views.editSet, name='editSets'),
]