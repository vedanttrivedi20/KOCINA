from django.urls import path
from . import views

urlpatterns = [

    path("", views.home, name="home"),

    path("about/", views.about, name="about"),

    path("contact/", views.contact, name="contact"),

    path("category/<str:keyword>/", views.category, name="category"),

    path("random/", views.random_recipe, name="random"),

]