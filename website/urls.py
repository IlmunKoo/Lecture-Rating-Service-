from django.contrib import admin
from django.urls import path
import web.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web.views.home, name='home'),
    path('board/', web.views.board, name='board'),
    path('detail/<int:id>', web.views.detail, name='detail'),
    path('ratings/', web.views.ratings, name='ratings'),
    path('login/', web.views.login, name='login'),
    path('signup/', web.views.signup, name='signup'),
]
