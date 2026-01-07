from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.detail, name="detalhe"),
    path("<int:id>/result/", views.results, name="resultado"),
    path("<int:id>/vote/", views.vote, name="voto"),
]