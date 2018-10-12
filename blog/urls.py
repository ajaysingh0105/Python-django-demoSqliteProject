from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/category/<slug:slug>/', views.post_category_wise, name='post_category_wise'),
	path('blog/<int:pk>/', views.post_detail1, name='post_detail1'),
	path('blog/<slug:slug>/', views.post_detail2, name='post_detail2'),
	path('blog/add', views.post_add, name='post_add'),
	path('blog/<int:pk>/edit/', views.post_edit1, name='post_edit'),
	path('blog/<slug:slug>/edit/', views.post_edit2, name='post_edit'),
	path('accounts/profile/', views.profile, name='profile'),
    path('accounts/registration/', views.registration, name='registration'),
]