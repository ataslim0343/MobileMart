from django.shortcuts import render
from django.db import connection

# Create your views here.
def viewprofile(request,un):
	query=connection.cursor()
	query.execute(f"""select username, first_name, last_name, email, Mobile, Aadhar,
	 Address, Pic from auth_user where username='{un}'""")
	s=query.fetchone()
	return render(request,'Customers/viewprofile.html',{'data':s})

def customerlist(request):
	query=connection.cursor()
	query.execute(f"select username, first_name, email, Mobile from auth_user where is_superuser='0'")
	s=query.fetchall()
	return render(request,"Customers/custlist.html",{'data':s})