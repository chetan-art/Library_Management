from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from Books.forms import BookAddForm
from django.contrib import messages
from .models import Add_Book_detail
#In this function we write logic to add a new student using the form
@login_required(login_url='http://127.0.0.1:8000/Loginup/')
def Add_Book(request):
    form = BookAddForm()
    if request.method == 'POST':  # we used the POST request
        form = BookAddForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'Add.html',{'form':form})

@login_required(login_url='http://127.0.0.1:8000/Loginup/')
def Detail(request):
    x = Add_Book_detail.objects.all()
    return render(request,'show.html',{'x':x})

@login_required(login_url='http://127.0.0.1:8000/Loginup/')
def DeleteBook(request,id):
    if request.method == 'POST':
        pi = Add_Book_detail.objects.get(pk = id)
        pi.delete()
        return redirect('http://127.0.0.1:8000/Details/')

@login_required(login_url='http://127.0.0.1:8000/Loginup/')
def EditBook(request,id):
    form = BookAddForm()
    if request.method == 'POST':
        pi = Add_Book_detail.objects.get(pk = id)
        form = BookAddForm(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/Details/')
    else:
        pi = Add_Book_detail.objects.get(pk=id)
        form = BookAddForm(instance=pi)
    return render(request, 'EditBook.html', {'form': form})