from django.contrib import admin
from django.urls import path,include,re_path
from . import views


urlpatterns = [
   path('',views.home,name='home'),
   path('contact-us',views.contact,name='contact'),
   path('product',views.product,name='product'),
   path('petrol-oil',views.petrol,name='petrol'),
   path('diesel-oil',views.diesel,name='diesel'),
   path('crude-oil',views.crude,name='crude'),
   path('become-a-partner',views.partner,name='partner'),
   path('thankyou',views.thankyou,name='thanku'),
   path('product',views.product,name='product'),
   path('motercycle',views.motercycle,name='motercycle'),
   path('comingsoon',views.comingsoon,name='comingsoon'),
   path('payment',views.payment,name='payment'),
   path('privacy-and-policy',views.privacy,name='privacy'),
   path('term-and-condition',views.term,name='term'),
   path('returnpolicy',views.returnpolicy,name='returnpolicy'),




]