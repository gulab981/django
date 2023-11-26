from django.urls import path
from . import views

urlpatterns = [

	path('base/',views.base , name = 'base'),
	path('navbar/',views.navbar , name = 'navbar'),
	path('mobile/',views.mobile , name = 'mobile'),
	path('desktop/',views.desktop , name = 'desktop'),

]