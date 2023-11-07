from django.shortcuts import render,reverse
from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def addProfileViewSet(request):
    if request.method == "POST":

        data = request.POST
        name =data.get('name')
        age =data.get('age')
        email = data.get('email')
        address = data.get('address')
        image = request.FILES.get('image')

        Profile.objects.create(
            name =name,
            age =age,
            email = email,
            address = address,
            image = image
        )
        if int(age) <18:
            messages.error(request,"Age cannot be less than 18!!!")
            return HttpResponseRedirect(reverse("add-profile"))
        return redirect('/profile-list/')
    queryset= Profile.objects.all()
    context = {'addProfile': queryset}
    return render(request, 'addProfile.html', context)

def profileListViewSet(request):
    queryset = Profile.objects.all()
    context = {'ProfileList': queryset}
    return render(request, 'profile_listing.html', context)

def deleteProfileViewSet(request, id):
    queryset = Profile.objects.get(id = id)
    queryset.delete()
    print(id)
    return redirect('/profile-list/')
def updateProfileViewSet(request, id):
    queryset = Profile.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        name =data.get('name')
        age = data.get('age')
        email = data.get('email')
        address = data.get('address')
        image = request.FILES.get('image')

        if int(age) <18:
            messages.error(request,"Age cannot be less than 18!!!")
            return HttpResponseRedirect(reverse("update-profile", args=[id]))
        queryset.name = name
        queryset.age = age
        queryset.email = email
        queryset.address = address
     
        if image:
            queryset.image= image
        queryset.save()
        return redirect('/profile-list/')
    print(queryset)
    context= {'profile': queryset}
    return render(request,'updateProfile.html',context)
        
