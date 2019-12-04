from xml.etree.ElementInclude import include
from django.conf.urls import url
from django.urls import path

from world.views import HomePageView

urlpatterns =[
    url(r'^$', HomePageView.as_view(), name = 'home'),

]



