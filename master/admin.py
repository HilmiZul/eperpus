from django.contrib import admin
from .models import Kategori, Penerbit, Buku

class KategoriAdmin(admin.ModelAdmin):
  list_display = ['nama', 'keterangan']
  search_fields = ['nama']
  list_per_page = 20

class PenerbitAdmin(admin.ModelAdmin):
  list_display = ['nama', 'telp', 'email', 'website', 'alamat']
  search_fields = ['nama', 'telp', 'alamat']
  list_per_page = 20
  
class BukuAdmin(admin.ModelAdmin):
  list_display = ['judul', 'tanggal', 'penulis', 'kategori', 'stok']
  list_filter = ('kategori_khusus', 'kategori', 'penerbit',)
  search_fields = ['judul', 'penulis', 'kategori', 'kategori_khusus']
  list_per_page = 20
  
  
admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Penerbit, PenerbitAdmin)
admin.site.register(Buku, BukuAdmin)
  
