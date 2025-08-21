from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'webapp/home.html')


def contact(request):
    return render(request,'webapp/contact-us.html')

def product(request):
    return render(request,'webapp/products.html')

def petrol(request):
    return render(request,'webapp/petrol.html')

def diesel(request):
    return render(request,'webapp/diesel.html')


def crude(request):
    return render(request,'webapp/crude.html')

def partner(request):
    return render(request,'webapp/partner.html')


def thankyou(request):
    return render(request,'webapp/thanku.html')


def motercycle(request):
    return render(request,'webapp/motercycle.html')


def comingsoon(request):
    return render(request,'webapp/coming-soon.html')


def payment(request):
    return render(request,'webapp/payment.html')


def privacy(request):
    return render(request,'webapp/privacy.html')


def term(request):
    return render(request,'webapp/term.html')



def returnpolicy(request):
    return render(request,'webapp/returnpolicy.html')