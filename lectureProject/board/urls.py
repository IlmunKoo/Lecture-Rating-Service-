from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name='board'),
    path('new', views.new, name='new'),
    path('new/create', views.create, name='create'),
    path('detail/<int:num>', views.detail, name='detail'),
    path('update/<int:num>', views.update, name='update'),
    path('delete/<int:num>', views.delete, name='delete'),
]