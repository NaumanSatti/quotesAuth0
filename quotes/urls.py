from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('deletequote/<qoute_id>', views.deletequote, name='deletequote'),
    path('editquote/<qoute_id>', views.editquote, name='editquote'),

]
