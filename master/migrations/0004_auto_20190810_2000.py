# Generated by Django 2.2.4 on 2019-08-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_auto_20190810_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='kategori_khusus',
            field=models.CharField(blank=True, choices=[('Umum', 'Umum'), ('TKJ', 'Teknik Komputer dan Jaringan'), ('RPL', 'Rekayasa Perangkat Lunak'), ('TBSM', 'Teknik dan Bisnis Sepeda Motor')], max_length=4),
        ),
    ]
