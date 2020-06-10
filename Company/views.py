from django.shortcuts import render,redirect
from django.db import connection
from django.contrib import messages


def addcom(request):
	if request.method=="POST":
		s=request.POST['companyname']
		query=connection.cursor()
		query=query.execute(f"insert into company(mobile) values('{s}')")
		return redirect('home')
	return render(request,"Company/addcompany.html")


# Create your views here.
