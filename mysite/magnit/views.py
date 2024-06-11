from django.shortcuts import render


def registration(request):
    return render(request, 'registration.html')


def vhod(request):
    return render(request, "vhodaition.html")