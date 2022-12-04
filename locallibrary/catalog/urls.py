from django.template.defaulttags import url
from django.urls import path
from . import views
from .views import BookListView, BookDetailView, AuthorListView, AuthorDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('allborrowed', views.LoanedBooksByLibraryAdmin.as_view(), name='all-borrowed'),
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),

    path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]
