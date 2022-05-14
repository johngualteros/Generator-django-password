from django.shortcuts import render
import random
# from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')
    
def about(request):
    return render(request, 'about.html')

def password(request):

    characters=list('abcdefghijklmnopqrstuvwxyz')
    
    generated_password=''

    length=int(request.GET.get('length'))

    if request.GET.get('upper_case'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('especial_characters'):
        characters.extend(list('-_¿?+*!@#%$^&()'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for char in range(length):
        generated_password+=random.choice(characters)


    return render(request, 'password.html',{'password':generated_password})
