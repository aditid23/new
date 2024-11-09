from django.shortcuts import render
def home(request):
    return render(request,'home.html',{'name':'Aditi'})
#dae2f0