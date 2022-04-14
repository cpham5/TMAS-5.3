from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), #Add index, main page, to urlpatterns
    path('add/', views.add, name='add'), #Add add, story addition form, to urlpatterns
]