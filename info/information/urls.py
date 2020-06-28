from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path("district/",views.district_list,name="district"),
    path("district/filter/",views.filter,name="filter"),
    
]

