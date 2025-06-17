from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context ={
        'bar':'Home',
        'judul':'SELAMAT DATANG ',
        'subJudul':'DI APLIKASI PINJAM RUANGAN ITJEN ESDM',
    
    }

    
    return render(request,'index.html', context)

