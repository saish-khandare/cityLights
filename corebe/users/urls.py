from django.urls import path

from .views import forgot_password, register, reset_password

urlpatterns = [
    path('register/', register),
    path('forgot-password/', forgot_password),
    path('reset-password/', reset_password),
]
