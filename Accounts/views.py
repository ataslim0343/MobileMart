from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import connection

# @login_required(login_url="/account/login/")

def login1(request):
	print(request.method)
	if request.method=="POST":
		form=AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return redirect("home")
	else:
		form=AuthenticationForm()
	return render(request,"Accounts/login.html",{'form':form})

def signup(request):
	if request.method=="POST":
		form=UserCreationForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect("home")
			# messages.success(request,f"Account is successfully created...!")
	else:
		form=UserCreationForm()
	return render(request,"Accounts/signup.html",{'form':form})


def logoutview(request):
	logout(request)
	return redirect("home")


def editpro(request):
	if request.method=="POST":
		un=request.POST['uname']
		fn=request.POST['fname']
		ln=request.POST['lname']
		em=request.POST['email']
		Aa=request.POST['aadhar']
		Add=request.POST['address']
		Mob=request.POST['mob']
		userdp=request.FILES['dp']
		f=FileSystemStorage()
		filename=f.save(userdp.name,userdp)
		uploaded_file_url=f.url(filename)
		c=connection.cursor()
		c.execute(f""" update auth_user set first_name='{fn}', last_name='{ln}', email='{em}', 
			Aadhar='{Aa}', Address='{Add}', Mobile='{Mob}', Pic='{uploaded_file_url}' where 
			username='{un}' """)
		return redirect("home")
	return render(request,"Accounts/editprofile.html")











