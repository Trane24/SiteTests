from django.urls import path
from . import views


urlpatterns = [
    path("", views.index),
    path("category/<int:category_id>/", views.get_category)
]
