from django.urls import path
from . import views

urlpatterns=[
	path('viewprofile/<str:un>/',views.viewprofile,name="viewpro"),
	path('customerlist/',views.customerlist,name="customerlist"),

]