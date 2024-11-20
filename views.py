from django.shortcuts import render, HttpResponse , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout

# Create your views here.
def aboutpage(request):
    return render(request, "about.html")

def io1page(request):
    return render(request, "io1.html")
def style2page(request):
    return render(request, "style2.html")
def orderpage(request):
    return render(request, "order.html")
def menupage(request):
    return render(request, "menu.html")
# def contactpage(request):
#     if request.method == 'POST':
#          user=request.POST.get('name')
#         #  pass1=request.POST.get('mobile')
#          user=authenticate(request, name=user)
#          if user is not None:
#             login(request, user)
#             return redirect('style2')
#          else:
#             return HttpResponse("password doesn't match")

#         #  print(user,pass1)

#     return render (request, 'contact1.html')
def contactpage(request):
    if request.method =='POST':
        name=request.POST.get('name')
        Email=request.POST.get('email')
        my_user=User.objects.create_user(name,Email)
        my_user.save()
        return redirect('style2')
    return render (request, 'contact1.html')
