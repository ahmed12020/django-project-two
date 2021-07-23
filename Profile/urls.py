from django.urls import path
from . import views

app_name = 'Profile'


urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profiledetails/<int:id>/', views.profile_details, name='profile_details'),
    path('likes_button/', views.likes_button, name='likes_button'),
    path('faves/<int:id>/', views.faves, name='faves'),
    path('all_fav/', views.all_fav, name='all_fav'),
    path('comments/<int:id>/', views.comments, name='comments'),
    path('setcookie/', views.setcookie, name='setcookie'),
    path('getcookie/', views.getcookie, name='getcookie'),
    path('delcookie/', views.delcookie, name='delcookie'),
    path('setsession/', views.setsession, name='setsession'),
    path('getsession/', views.getsession, name='getsession'),
    path('delsession/', views.delsession, name='delssession'),
    path('login/', views.Login.as_view(), name='login'),
    path('sign/', views.sign, name='sign'),
]
