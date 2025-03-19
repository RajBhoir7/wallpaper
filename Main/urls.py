# MainApp URLS



from Main import views
from django.contrib import admin
from django.urls import path




urlpatterns = [
    path('',views.home,name='home'),
    path('about_us',views.about_us,name='about_us'),
    path('login',views.user_login_register,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('connect-us',views.connect_us,name='connect_us'),
    path('/<choice>',views.selected_wallpapers,name='selected_wallpapers')
    
]