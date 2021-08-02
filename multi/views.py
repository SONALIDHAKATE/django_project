from django.shortcuts import render
from.models import *
# Create your views here.
def index(request):
    var=abc.objects.all()
    print (var)
    context={'var':var}
    for i in var:
        print(i.name)
    return render(request,'index.html',context)
 

def res(request):
    a=request.GET['number1']
    z=eval(a)
    
    return render(request,'result.html',{'key':z})