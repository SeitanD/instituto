from django.urls import path
from .views import index, crud
from alumnos import views

urlpatterns = [
    path('', index, name='index'),
    path('crud', views.crud, name='crud'),
    path('alumnos/alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos/alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos/alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnos/alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),

    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd', views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>', views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),
]