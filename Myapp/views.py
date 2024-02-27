from django.shortcuts import render


def Home(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Chocolate(request):
    return render(request, 'chocolate.html')


def Testimonial(request):
    return render(request, 'testimonial.html')


def Contact(request):
    return render(request, 'contact.html')

