from django.urls import path
from . import views
urlpatterns=[
	path('addmob/',views.addmob,name="addmob"),
	path('moblist/',views.moblist,name="moblist"),
	path('mobdet/<int:mod>/',views.mobdet,name="mobdet"),
	path('updatemob/<str:mod>/',views.updatemob,name="updatemob"),
	path('updatemob2/<str:mod>/',views.updatemob2,name="updatemob2"),
	path('confdelmob/<str:mod>/',views.confdel,name="deletemob"),
	path('delmob/<str:mod>/',views.delmob,name="delmob"),
	path('filtermobs/',views.filtermobs,name="filtermobs"),
	path('addtocart/<int:>',views.addtocart,name="addtocart"),
	path('viewcart/<int:>',views.viewcart,name="viewcart"),
	path('cartremove/<int:>',views.cartremove,name="cartremove"),
	

]