from django.conf.urls import url

from . import views

app_name = "geogebra"
urlpatterns = [
    # ex: /geogebra/
    url('^$', views.index, name='index'),
]