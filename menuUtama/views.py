from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from .forms import MenuUtama
#from .models import PostData 

def index(request):
    
    #posts = PostData.objects.all()
    #print(posts)
    menu = MenuUtama(request.POST or None)
    
    if request.method == "POST":
        if menu.is_valid():
            menu.save()
    
        #PostData.objects.create(

        #    nama = request.POST.get('nama'),
        #    satker = request.POST.get('satker'),
        #    ruangan = request.POST.get('ruangan'),
        #    waktu = request.POST.get('waktu'),
        #    keterangan = request.POST.get('keterangan'),
        #    isi = menu.save()
        #)
        
        return HttpResponseRedirect("/blog/")

    context = {
        'bar':'Form Pengisian ',
        'judul':'HALAMAN PENGISIAN FORM ',
        'subJudul': 'PINJAM RUANGAN',
        'form': menu
       
    }

    return render(request, 'menuUtama/index.html', context)
    