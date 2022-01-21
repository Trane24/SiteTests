from django.urls import path
from . import views

urlpatterns = [
    path("category/<int:category_id>/", views.get_category, name="category"),
    path("", views.index, name="home")
]
