from django.conf.urls import url
from . import views

urlpatterns = [
path(r'^$', views.index, name = 'index')
]
