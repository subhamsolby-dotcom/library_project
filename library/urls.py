from django.urls import path
from . import views

urlpatterns = [

path('', views.home, name='home'),

path('add-book/', views.add_book, name='add_book'),

path('books/', views.book_list, name='book_list'),

path('add-member/', views.add_member, name='add_member'),

path('borrow-book/', views.borrow_book, name='borrow_book'),

]