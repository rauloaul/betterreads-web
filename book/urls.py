from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('<int:book_id>/add_reviews', views.add_review, name='add_review'),
    #path('curator-section/', views.curator_section, name='curator_section'),
    path('<int:book_id>/get-reviews/', views.get_reviews, name='get_reviews'),

]
