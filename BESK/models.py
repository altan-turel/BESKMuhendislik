from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(("Görev Adı"), max_length=50)
    def __str__(self):
        return self.name
    
class Birim(models.Model):
    name = models.CharField(("Görev Adı"), max_length=50)
    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(("Personel Adı"), max_length=50)
    job = models.ForeignKey("Job", verbose_name=("Peronel Görevi"), on_delete=models.CASCADE)
    image = models.FileField(("Personel Fotoğrafı"), upload_to=None, max_length=100)
    def __str__(self):
        return self.name
    
class Program(models.Model):
    name = models.CharField(("Program Adı"), max_length=50)
    job = models.ForeignKey("Birim", verbose_name=("Program Görevi"), on_delete=models.CASCADE)
    image = models.FileField(("Program Fotoğrafı"), upload_to=None, max_length=100)
    def __str__(self):
        return self.name
    
class Proje(models.Model):
    year = models.CharField(("Proje Yılı"), max_length=4)
    name = models.CharField(("Proje Adı"), max_length=255)
    who = models.CharField(("Proje Kimin?"), max_length=255)
    start = models.CharField(("Proje Başlama Tarihi"), max_length=10)
    finish = models.CharField(("Proje Bitiş Tarihi"), max_length=10)
    price = models.DecimalField(("Proje Tutarı"), max_digits=9, decimal_places=2)
    def __str__(self):
        return self.name
    
class Faaliyet(models.Model):
    name = models.CharField(("Faaliyet Alanları"), max_length=255)
    def __str__(self):
        return self.name
    
class FaaliyetKonu(models.Model):
    faaliyet = models.ForeignKey("Faaliyet", verbose_name=("Faaliyet Alanı"), on_delete=models.CASCADE)
    name = models.CharField(("Faaliyet Konusu"), max_length=255)
    def __str__(self):
        return self.name
    
class ProjectImage(models.Model):
    image = models.FileField(("Proje Görseli"), upload_to=None, max_length=100)
    name = models.CharField(("Proje Adı"), max_length=255)
    who = models.CharField(("Proje Kime"), max_length=255)
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(("Kullanıcı Adı"), max_length=255)
    phone = models.CharField(("Kullanıcı Telefonu"), max_length=255, blank=True, null=True)
    email = models.CharField(("Kullanıcı Email"), max_length=255)
    message = models.TextField(("Kullanıcı Adı"))
    
    def __str__(self):
        return self.name