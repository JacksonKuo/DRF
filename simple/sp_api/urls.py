from django.urls import path
from sp_api import views

urlpatterns = [
    path('notes/', views.note_list),
]
    