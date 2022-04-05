from django.urls import path
from Books.views import Add_Book,Detail,EditBook
from Books import views
urlpatterns = [
    path('Add_Book/', Add_Book,name = 'AddBook'),
    path('Details/',Detail,name='Details/'),
    path('<int:id>/',views.EditBook,name = 'EditBook'),
    path('delete/<int:id>/',views.DeleteBook,name = 'DeleteBook'),
    ]