from django.urls import path
from . import views

urlpatterns = [
    path('',views.create,name='create'),
    path('one/<int:pk>',views.display,name='display'),
    path('index',views.index,name='index'),
    path('two/<int:ab>',views.edit,name='edit'),
    path('history',views.history,name='history'),
    path('delete/<int:hi>',views.delete,name='delete'),
]