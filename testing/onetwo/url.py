from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('video/', views.videos),
    path('sin/', views.sin, name='sin'),
    path('lessons/', views.lesson, name='lessons'),
    path('subVD/', views.subvideo),
    path('notes/', views.note),
    path('try/', views.tryy),
    path('live/', views.live),

    path('sin/', views.sin, name='sin'),
    path('reg/', views.reg),
    path('signout/',views.sign_out, name='sign out')
]