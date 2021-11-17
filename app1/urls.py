from django.urls import path
from . import views
urlpatterns=[
    path('', views.index),
    path('bio', views.bio),
    path('hardestYear', views.hardestYear),
    path('anthologies', views.anthologies),
    path('contact', views.contact),

]