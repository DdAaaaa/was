from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logging/',views.quarter_block, name='logging'),
    # path('signin/', ),
    # path('signup/', ),
    # path('summary/')
]