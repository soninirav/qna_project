from django.urls import path
from App_Users import views

urlpatterns = [
    path('register/',views.register,name='register'),

]
