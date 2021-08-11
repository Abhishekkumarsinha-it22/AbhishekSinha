from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('profp/', views.profpf, name='profront'),
    path('profp/categories/<str:cats>/', views.categories1, name='categories'),
    path('single/<int:blocks>/', views.singleview)

]