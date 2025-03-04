from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
]