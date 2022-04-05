from django.shortcuts import render,redirect,HttpResponseRedirect

# Create your views here.
def Home(request): # We create a Function

    return render(request,'home.html')  # we return A html file



