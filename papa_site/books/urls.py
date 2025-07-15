from django.urls import path
from . import views


urlpatterns = [
   path('books', views.books, name='books'),
   # path('livres/<int:livre_id>/commander/', views.commander_livre, name='commander_livre'),


]
