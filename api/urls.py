# api/urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path('blog', views.PostListView.as_view()),
    path('blog/category', views.CategoryListView.as_view()),
    path('blog/category/posts', views.CategoryWisePostView.as_view()),
    path('blog/add', views.PostAddView.as_view()),
    path('blog/single', views.PostSingleView.as_view()),
    path('blog/single/update', views.PostSingleUpdateView.as_view()),
    path('blog/single/delete', views.PostSingleDeleteView.as_view()),
    #url( r'^todos/(?P<pk>\d+)/$',TodoViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),name='todo-detail', )
    path('rest-auth/', include('rest_auth.urls')),
]