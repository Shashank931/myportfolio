from django.urls import path
from myportfolio.views import home
urlpatterns = [
    path("", home , name='home' ),
]