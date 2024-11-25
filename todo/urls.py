from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addtodo', views.addtodo, name='addtodo'),
    path('deletetodo/<int:id>/', views.deletetodo, name='deletetodo'),
    path('edittodo/<int:id>/', views.edittodo, name='edittodo'),
]