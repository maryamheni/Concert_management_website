from django.shortcuts import render,redirect
from .forms import SubmitForm
from django.contrib import messages

# Create your views here.
def home(request):
   if request.method=='POST':
      form=SubmitForm(request.POST)
      if form.is_valid():
          form.save()
          name=form.cleaned_data.get('first_name')
          messages.success(request,f'Hi ,congratulation Your Application has been submited with success for{name}')
          return redirect('about')
   else:
       form=SubmitForm()
   context={
       'form':form
   }
   return render(request,"form/home.html",context)
def about(request):
    return render(request,"form/about.html")