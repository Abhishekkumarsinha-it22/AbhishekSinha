from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blogview),
    path('blogpage',views.blogpage),
    path('singlepage/<int:id>/', views.blogsinglepage),
    path('categories/<str:cats>', views.categ)


]