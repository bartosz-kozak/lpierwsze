from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def lpierwsze(request):
    n = 0 # zmienna do obliczenia liczby liczb pierwszej
    l = [] # lista liczb pierwszych
    p1 = int(request.GET['p1'])
    p2 = int(request.GET['p2'])
    if p1 == 1 or p2 == 1:
        return render(request, 'error.html')
    if p1 > 10000 or p2 > 10000:
        return render(request, 'error.html')
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
                if c == 0:
                    if b < a: # spełnienie warunku oznacza, że liczba jest podzielna przez dzielnik mniejszy od liczby czyli nie jest liczbą pierwszą
                        d = 1
                    else: # spełnienie warunku if c == 0 i nie spełnienie warunku b<0 oznacza, że liczba jest liczbą pierwszą, program dodaje 1 do liczby liczb pierwszych
                        n = n+1
                        d = 1
                        l.append(a)

        return render(request, 'lpierwsze.html',{'p1':p1,'p2':p2,'n':n,'l':l})

def liczby(request):
    return render(request, 'liczby.html')