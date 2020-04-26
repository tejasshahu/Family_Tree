from django.urls import path, include
from . import views


urlpatterns = [
	path(r'', views.index, name='index'),
	path(r'parents/', views.display_parents, name='display_parents'),
	path(r'siblings/', views.display_siblings, name='display_siblings'),
	path(r'children/', views.display_children, name='display_children'),
	path(r'grandparents/', views.display_grandparents, 
		 name='display_grandparents'),
	path(r'cousins/', views.display_cousins, name='display_cousins'),
]
