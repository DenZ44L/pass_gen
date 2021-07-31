from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def yaprak(request):
    return render(request, 'yarrak/home.html')

alphabet = ['q','w','e','r','t','y','u','ı','o','p','a','s','d','f','g','h','j','j','k','l','z'
         ,'x','c','v','b','n','m']

numbers = [1,2,3,4,5,6,7,8,9,0]

symbols= ['!','£','#','%','&','+','<','>','?']

def pasword(request):

    lenghth = int(request.GET.get('lenght'))

    wholepass = []
    wholepassstr = ''


    if request.GET.get('numbers') == 'on':
        numbool = True
    else :
        numbool = False

    if request.GET.get('symbols') == 'on':
        symbool = True
    else :
        symbool = False




    if (numbool) & (symbool):
        wholepass += numbers+alphabet+symbols

    elif numbool==True:
        wholepass = numbers+alphabet
    elif symbool==True:
        wholepass = symbols+alphabet
    else:
        wholepass = alphabet


    random.shuffle(wholepass)
    final = wholepass[:lenghth]
    for each in final:
        wholepassstr += str(each)

    return render(request, 'yarrak/pasword.html', {'pasword': wholepassstr})

def about(request):
    return render(request, 'yarrak/about.html')
