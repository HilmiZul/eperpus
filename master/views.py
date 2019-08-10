from django.shortcuts import render
from .models import Buku

def index(request):
  books = Buku.objects.all().order_by('-tanggal', 'kategori_khusus', 'kategori' )
  return render(request, 'index.html', {'books':books})
