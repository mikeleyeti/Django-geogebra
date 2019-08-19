from django.urls import path

from . import views

urlpatterns = [
    # ex: /geogebra/
    path('', views.index, name='index'),
]
