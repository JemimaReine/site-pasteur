from django.urls import path
from . import views


urlpatterns = [
   path('newsletter/', views.inscrire_newsletter, name='newsletter'),

]
