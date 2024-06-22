from django.urls import path
from .views import index, crud, alumnosAdd, alumnos_del, alumnos_findEdit, alumnosUpdate

urlpatterns = [
    path('', index, name='index'),
    path('crud', crud, name='crud'),
    path('alumnosAdd', alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', alumnosUpdate, name='alumnosUpdate'),


]