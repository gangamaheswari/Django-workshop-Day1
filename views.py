from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def he(request):
    return HttpResponse("<h1>Hello guys...Welcome to django workshop</h1>")

def sam(request):
	return HttpResponse("<h2 style=color:green;background-color:hotpink;font-size:45px;font-style:italic> <center>Hello world!</center></h2>")

	

def dynamic(request,a,b):
    return HttpResponse("<h2><center>My Roll No is:{} and My Name is : {}</h2></center>".format(a,b))

