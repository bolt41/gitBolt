from django.urls import path
from .views import HomePageView, AddTransaction

urlpatterns = [
    path('', HomePageView, name='home'),
    path('add', AddTransaction, name='add_trans')

]
