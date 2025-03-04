from django.urls import path
from . import views


urlpatterns = [
    path('getInfoDatatable/', views.getInfoDatatable, name="getInfoDatatable"),
    # path('getRowsPaysForShippingMail/<str:database>', views.getRowsPaysForShippingMail, name="getRowsPaysForShippingMail"),
    # path('allMailsCustomer/<str:databaseSelect>', views.allMailsCustomer, name="allMails"),
    # path('correospan/',views.correospan, name="correospan"),
]