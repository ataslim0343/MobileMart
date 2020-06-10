from django.shortcuts import render,redirect
from django.contrib import messages
from django.db import connection
from django.core.files.storage import FileSystemStorage

def addmob(request):
	if request.method=="POST":
		mob=request.POST['mobile']
		mod=request.POST['model']
		pr=request.POST['price']
		qty=request.POST['quantity']
		batt=request.POST['battery']
		ch=request.POST['charger']
		hs=request.POST['headset']
		mem=request.POST['memory']
		dc=request.POST['datacable']
		Pic=request.FILES['picture']
		f=FileSystemStorage()
		filename=f.save(Pic.name,Pic)
		uploaded_file_url=f.url(filename)
		c=connection.cursor()
		c.execute(f""" insert into mobile(mobile,model,price,quantity,charger,
			battery,headset,memory,datacable,pic) values('{mob}','{mod}','{pr}','{qty}',     
			'{ch}','{batt}','{hs}','{mem}','{dc}','{uploaded_file_url}') """)


		return redirect("home")
	c=connection.cursor()
	c.execute(f"select mobile from company")
	s=c.fetchall()
	return render(request,"Mobiles/addmobiles.html",{'data':s})


def moblist(request):
	c=connection.cursor()
	c.execute(f"select mobile,model,price,id from mobile")
	d=c.fetchall()
	return render(request,"Mobiles/mobilelist.html",{'data':d})

def mobdet(request,mod):
	c=connection.cursor()
	c.execute(f""" select mobile,model,price,quantity,charger,battery,headset,
		memory,datacable,pic from mobile where id='{mod}' """)
	s=c.fetchone()
	return render(request,"Mobiles/mobiledetails.html",{'data':s})

def updatemob(request,mod):
	c=connection.cursor()
	c1=connection.cursor()
	c.execute(f""" select mobile,model,price,quantity,charger,battery,headset,
		memory,datacable,pic from mobile where model='{mod}' """)
	s=c.fetchone()
	c1.execute(f""" select DISTINCT(mobile) from mobile""")
	s1=c1.fetchall()
	return render(request,"Mobiles/updatemobiles.html",{'data':s,'data2':s1})

def updatemob2(request,mod):
	if request.method=="POST":
		mob=request.POST['mobile']
		mod=request.POST['model']
		pr=request.POST['price']
		qty=request.POST['quantity']
		batt=request.POST['battery']
		ch=request.POST['charger']
		hs=request.POST['headset']
		mem=request.POST['memory']
		dc=request.POST['datacable']
		Pic=request.FILES['picture']
		f=FileSystemStorage()
		filename=f.save(Pic.name,Pic)
		uploaded_file_url=f.url(filename)
		c=connection.cursor()
		c.execute(f""" update mobile set mobile='{mob}', model='{mod}', 
			price='{pr}', quantity='{qty}', charger='{ch}',
			battery='{batt}', headset='{hs}', memory='{mem}', datacable='{dc}',
			pic='{uploaded_file_url}' where model='{mob}' """) 
		return redirect("home")
	return render(request,"Mobiles/updatemobiles,html")

def confdel(request,mod):
	p=connection.cursor()
	p.execute(f"select modal from mobile where modal={mod}")
	s=p.fetchone()
	return render(request,"Mobiles/deletemobiles.html",{'data':s})

def delmob(request,mod):
	p=connection.cursor()
	p.execute(f"delete from mobile where model='{mod}'")
	return redirect("moblist")


def filtermobs(request):
	c=connection.cursor()
	r=f"select * from mobile"
	if request.method=="POST":
		mob=request.POST['mob']
		mod=request.POST['mod']
		frm=request.POST['frm']
		to=request.POST['to']

		if frm:
			r=f""" select * from mobile where mobile like '%{mob}%' and model like 
			 '%{mod}%' and (price>={frm} and price<={to}) """
		else:
			r=f""" select * from mobile where mobile like '%{mob}%' and model like 
			 '%{mod}%' """
	c.execute(r)
	p=c.fetchall()
	return render(request,"Mobiles/filtermobiles.html",{'data':p})

# @login_required
def addtocart(request,id):
	c=connection.cursor()
	c.execute(f"select * from mobile where id='{id}'")
	r=c.fetchone()
	cart=request.session.get('cart',{})
	cart[id]=r
	request.session['cart']=cart
	messages.success(request,f"Added to cart...Check you cart now..!!")
	return redirect("cfilmob") 
	# cfilmob=customer filter mobile-- To be add for user to search the mobiles
# @login_required
def viewcart(request):
	cart=request.session.get('cart',{})
	return render(request,"Mobile/viewcart.html",{'data':cart.values()})
# @login_required
def cartremove(request,id):
	print(request.session['cart'][str(id)])
	try:
		del request.session['cart'][str(id)]
	except Exception as e:
		print("Hello")
	request.session.modified=True
	return redirect('viewcart')

















