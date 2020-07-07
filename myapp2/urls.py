from django.conf.urls import url
from myapp2 import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
