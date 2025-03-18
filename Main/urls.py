# MainApp URLS



from Main import views
from django.contrib import admin
from django.urls import path




urlpatterns = [
    path('',views.home,name='home'),
    path('login',views.user_login,name='login'),
    path('connect-us',views.connect_us,name='connect_us')
    
]