
from django.urls import path
from app import views
app_name= 'app'
urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.handle_login,name='handle_login'),
    path('logout/',views.handle_logout,name='handle_logout'),
    
]
