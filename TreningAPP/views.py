from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):

    uzytkownik = request.user.profiluzytkownika

    jednorazowa = JednorazowaPlatnosc.objects.get(id=1)



    context = {

    }

    return render(request, 'TreningAPP/index.html', context)