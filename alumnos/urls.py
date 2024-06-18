from django.urls import path
from .views import index,crud
from . import views

urlpatterns = [
    path('',index,name='index'),
    path('crud',views.crud, name='crud'),

]