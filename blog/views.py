from django.shortcuts import render

# Create your views here.
from menuUtama.models import PostData

def index(request):
    
    posts = PostData.objects.all()
    
    context = {
        'bar':'Riwayat Peminjaman',
        'judul':'BERIKUT DAFTAR PEMINJAM RUANGAN',
        'form': posts
        
    }
    return render(request, 'blog/index.html', context)
