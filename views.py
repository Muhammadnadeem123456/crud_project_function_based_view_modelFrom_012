from django.shortcuts import render, HttpResponsePermanentRedirect
from .forms import studentregisteration
from .models import user
# Create your views here.
#view function for add and show....items
def add_show(request):
    if request.method=='POST':
        fm=studentregisteration(request.POST)
        if fm.is_valid():
         
        #  nam=fm.cleaned_data['name']
        #  ema = fm.changed_data['email']
        #  ema=fm.changed_data['email']
        #  pas=fm.changed_data['password']
        #  reg=user(name=nam, email=ema, password=pas)
         fm.save()
         fm=studentregisteration()
         
    else:
        fm=studentregisteration()
    stu=user.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'student':stu})
#view function for delete items .....
def delete_data(request,id):
   if request.method=='POST':
      pi=user.objects.get(pk=id)
      pi.delete()
      return HttpResponsePermanentRedirect('/')
   
#view function for update/edit items
def update_data(request,id):
    if request.method == "POST":
       pi=user.objects.get(pk=id)
       pm=studentregisteration(request.POST,instance=pi)
       if pm.is_valid():
         pm.save()
    else:
       pi=user.objects.get(pk=id)
       pm=studentregisteration(instance=pi)
       
 
    return render(request,'enroll/updatestudent.html/',{'form':pm})
    