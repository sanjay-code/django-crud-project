from django.shortcuts import render, HttpResponseRedirect
from .forms import InputData
from .models import People_data
from django.contrib import messages
# Create your views here.

def HomeView(request):
	form = People_data.objects.all()

	return render(request,'crud/index.html',{'form':form})

def Add_Item(request):
	if request.method == "POST":
		form = InputData(request.POST)
		if form.is_valid():
			nm = form.cleaned_data['name']
			em = form.cleaned_data['email']
			roll = form.cleaned_data['phone']
			user = People_data(name=nm,email=em,phone=roll)
			user.save()
			messages.success(request,'succesfully add your data')
			form = InputData()



	else:
		form = InputData()
	return render(request,'crud/add_data_here.html',{'fm':form})


def count_total(request):
	form = People_data.objects.all()
	coun = form.count()
	context = {'coun':coun,}
	return render(request, 'crud/total.html',context)

def Edit_item(request, id):
	if request.method == "POST":
		pi = People_data.objects.get(pk=id)
		fm = InputData(request.POST, instance=pi)
		if fm.is_valid():
			fm.save()
			messages.success(request,'update succesfully')
			return HttpResponseRedirect('/')
	else:
		pi = People_data.objects.get(pk=id)
		fm = InputData(instance=pi)
	return render(request, 'crud/EditData.html',{'form':fm})

def Delete_item(request, id):
	pi = People_data.objects.get(pk=id)
	if request.method == "POST":
		pi.delete()
		messages.success(request,'item deleted succesfully')
		return HttpResponseRedirect('/')

	return render(request, 'crud/Delete_data.html',{'pi':pi})

def Find_data(request):
	search = request.GET['search']
	all_post = People_data.objects.filter(name__icontains=search)
	context = {'all_post':all_post}
	return render(request,'crud/search_item.html',context)
