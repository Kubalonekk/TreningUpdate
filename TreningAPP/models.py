from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation



class ProfilUzytkownika(models.Model):
    uzytkownik = models.OneToOneField(User, on_delete=models.CASCADE)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    email = models.EmailField()
    data_zalozenia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.imie} {self.nazwisko}. Identyfikator: {self.id}"
    

class KontoBankowe(models.Model):
    profil_uzytkownika = models.ForeignKey(ProfilUzytkownika, on_delete=models.CASCADE)
    numer_konta = models.PositiveIntegerField()
    stan_konta = models.PositiveIntegerField()

    def __str__(self):
        return f"Konto uzytkownika: {self.profil_uzytkownika.imie} {self.profil_uzytkownika.nazwisko}, o numerze konta {self.numer_konta}"


class Zakup(models.Model):
    SPOSOB_PLATNOSCI = (
        ('','Podaj formę zapłaty'),
        ('Gotowka', 'Gotówka'),
        ('Przelew', 'Przelew'),
        ('Karta','Karta kredytowa'),
    )
    ODBIORCA = (
        ('Firma', 'Firma'),
        ('Fizyczna','Osoba fizyczna'),
    )

    kupujacy = models.ForeignKey(KontoBankowe, on_delete=models.CASCADE, null=True)
    do_zaplaty = models.PositiveIntegerField(null=True)
    tytulem = models.CharField(max_length=200)
    odbiorca = models.CharField(max_length=20, choices=ODBIORCA, null=True)
    sposob_platnosci = models.CharField(max_length=50, choices=SPOSOB_PLATNOSCI,)
    data_zakupu = models.DateTimeField(auto_now_add=True, null=True)

    content_type =   models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object=GenericForeignKey('content_type', 'object_id')


    def __str__(self):
        return f"{self.kupujacy.profil_uzytkownika.imie} {self.kupujacy.profil_uzytkownika.nazwisko} Numer konta: {self.kupujacy.numer_konta} . Platnosc: {self.sposob_platnosci} Identyfikator platnosci: {self.id}"
    


class Leasing(models.Model):
    ilosc_rat = models.PositiveIntegerField(null=True)
    data_rozpoczecia = models.DateTimeField(null=True)
    oplata_wstepna = models.PositiveIntegerField(null=True)
    zakup = GenericRelation(Zakup)
    nip = models.PositiveIntegerField(null=True)
    nazwa_firmy = models.CharField(max_length=150, null=True)


class Raty(models.Model):
    imie = models.CharField(max_length=100, null=True)
    nazwisko = models.CharField(max_length=100, blank=True)
    pesel = models.PositiveIntegerField(null=True)
    ilosc_rat = models.PositiveIntegerField(null=True)
    zakup = GenericRelation(Zakup)


class JednorazowaPlatnosc(models.Model):
    tytulem = models.CharField(max_length=200)
    zakup = GenericRelation(Zakup)
    
class RataLeasingu(models.Model):
    leasing = models.ForeignKey(Leasing, on_delete=models.CASCADE, null=True)
    wysokosc_raty = models.PositiveIntegerField()
    data_splaty = models.DateTimeField()

class PojedynczaRata(models.Model):
    raty = models.ForeignKey(Raty, on_delete=models.CASCADE, null=True)
    wysokosc_raty = models.PositiveIntegerField()
    data_splaty = models.DateTimeField()

















    



