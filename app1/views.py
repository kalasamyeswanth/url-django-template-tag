from django.shortcuts import render

# Create your views here.
def link1(request):
    return render(request,'web1.html')

def link2(request):
    return render(request,'web2.html')