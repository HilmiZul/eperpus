from django.db import models

class Kategori(models.Model):
  nama = models.CharField(max_length=50)
  keterangan = models.TextField()
  def __str__(self):
    return self.nama
  
class Penerbit(models.Model):
  nama = models.CharField(max_length=50)
  telp = models.IntegerField(blank=True)
  email = models.CharField(max_length=100, blank=True)
  website = models.CharField(max_length=100, blank=True)
  alamat = models.TextField(blank=True)
  def __str__(self):
    return self.nama

class Buku(models.Model):
  kategori_khusus_choices = (
    ('Umum', 'Umum'),
    ('TKJ', 'Teknik Komputer dan Jaringan'),
    ('RPL', 'Rekayasa Perangkat Lunak'),
    ('TBSM', 'Teknik dan Bisnis Sepeda Motor'),
  )
  kelas_choices = (
    ('X', 'X (Sepuluh)'),
    ('XI', 'XI (Sebelas)'),
    ('XII', 'XII (Dua belas)'),
  )
  pegangan_choices = (
    ('Guru', 'Guru'),
    ('Siswa', 'Siswa'),
    ('Guru/Siswa', 'Guru/Siswa'),
  )
  kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
  kategori_khusus = models.CharField(max_length=4, choices=kategori_khusus_choices, blank=True)
  isbn = models.CharField(max_length=100)
  tanggal = models.DateTimeField(auto_now_add=True)
  kode_buku = models.CharField(max_length=40)
  judul = models.CharField(max_length=80)
  kelas = models.CharField(max_length=15, choices=kelas_choices, blank=True, null=True)
  pegangan = models.CharField(max_length=10, choices=pegangan_choices, blank=True, null=True)
  penulis = models.CharField(max_length=80)
  penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE)
  stok = models.IntegerField()
  lokasi = models.CharField(max_length=30, blank=True)
  keterangan = models.TextField(blank=True)
  cover = models.ImageField(upload_to='buku/cover/', blank=True)
  def __str__(self):
    return self.judul
  
