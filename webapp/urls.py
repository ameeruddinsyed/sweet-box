from django.contrib import admin


from django.urls import path
from webapp import views
#create here urls:

urlpatterns=[
    
   path('',views.first_view) 
    
    
]