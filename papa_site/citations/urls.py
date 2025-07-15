from django.urls import path
from . import views


urlpatterns = [
   path('citations', views.citations, name='citations'),
   path('<int:pk>/', views.citation_detail, name='citation_detail'),

]
