from django.http import HttpResponse
from django.shortcuts import render
import datetime

rok = str(datetime.datetime.now().year)

def home(request):
    return render(request, 'home.html',{'tytul':'Znajdź liczby pierwsze','rok':rok})

def lpierwsze(request):
    n = 0 # zmienna do obliczenia liczby liczb pierwszej
    l = [] # lista liczb pierwszych
    p1 = request.GET['p1']
    p2 = request.GET['p2']
    if len(p1) == 0 or len(p2) == 0:
        return render(request, 'error.html',{'tytul':'Błąd','rok':rok})
    if 'e' in p1 or 'e' in p2:
        p1 = float(p1)
        p2 = float(p2)
        #return render(request, 'error.html',{'tytul':'Błąd'})
    p1 = int(p1)
    p2 = int(p2)
    if p1 <= 1 or p2 <= 1:
        return render(request, 'error.html',{'tytul':'Błąd','rok':rok})
    if p1 > 100000 or p2 > 100000:
        return render(request, 'error.html',{'tytul':'Błąd','rok':rok})
    else:
        if p1 > p2:
            p3 = p1
            p1 = p2
            p2 = p3

        for a in range(p1,p2):
            b = 2 # zmienna używana do dzielenia liczby
            d = 0 # zmienna "przerywacz pętli"
            while d < 1:
                c = a%b # zmienna - reszta z dzielenia
                if c != 0: # jeżeli warunek spełniony dodaje do dzielnika 1
                    b = b+1
                    if b > a**0.5: # sprawdza liczby do pierwiastka z a jeżeli nie ma dizelnika w tym przedziale to liczba jest liczbą pierwszą
                        n = n+1
                        d = 1
                        l.append(a)
                if c == 0:
                    if b < a: # spełnienie warunku oznacza, że liczba jest podzielna przez dzielnik mniejszy od liczby czyli nie jest liczbą pierwszą
                        d = 1
                    else: # spełnienie warunku if c == 0 i nie spełnienie warunku b<0 oznacza, że liczba jest liczbą pierwszą, program dodaje 1 do liczby liczb pierwszych
                        n = n+1
                        d = 1
                        l.append(a)

        return render(request, 'lpierwsze.html',{'p1':p1,'p2':p2,'n':n,'l':l,'tytul':'Liczby pierwsze w przedziale','rok':rok})

def liczby(request):
    return render(request, 'liczby.html',{'tytul':'O liczbach pierwszych','rok':rok})
#def ulam(request):
    
