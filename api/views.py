from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.conf import settings
from urllib.parse import urljoin
import shutil
import os.path

# Create your views here.
from rest_framework import generics
from blog.models import Post, Category
from . import serializers

class BlogPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'limit'
    max_page_size = 100
        
class PostListView(generics.ListAPIView):
    #Method1
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    pagination_class = BlogPagination
    
    #Method2
    #def get(self, *args, **kwargs):
        #queryset = Post.objects.all()
        #serializer_class = serializers.PostSerializer(queryset, many=True)
        #pagination_class = BlogPagination
        #return Response({'status': 'success','data': serializer_class.data, 'msg':''})
        
    
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = BlogPagination

class CategoryWisePostView(generics.RetrieveAPIView):
    def post(self, *args, **kwargs):
        cId = self.request.data['pk']
        if Category.objects.filter(pk=cId).exists():
            category = Category.objects.get(pk=cId)
            post = Post.objects.filter(category=category)
            serializer = serializers.PostSerializer(post, many=True)
            pagination_class = BlogPagination
            
            return Response({'status': 'success','data': serializer.data, 'msg':''})
        else:
            return Response({'status': 'error', 'data': '', 'msg': 'Invalid Post!'})

class PostAddView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer
    def post(self, *args, **kwargs):
        post = self.request.data
        serializer = serializers.PostSerializer(data=post)
        if serializer.is_valid():
            serializer.save()
            #Custom code for update image path
            #done = serializer.data
            #baseUrl = settings.BASE_URL
            #basePath = settings.STATIC_ROOT
            #oldPath = done['featured_image']
            #newPath = oldPath.replace('None', str(done['pk']))
            #newPath = oldPath.replace('None', 'xyz')
            #shutil.move(os.path.join(basePath, oldPath), os.path.join(basePath, newPath))
            #Post.objects.filter(pk=done['pk']).update(featured_image=newPath)
            #done['url'] = urljoin(baseUrl, newPath)
            return Response({'status': 'success','msg': 'Blog Added Successfully', 'data': serializer.data})
        return Response({'status': 'error','msg': serializer.errors})
        

class PostSingleView(generics.RetrieveAPIView):
    serializer_class = serializers.PostSerializer
    def post(self, *args, **kwargs):
        pkId = self.request.data['pk']
        if Post.objects.filter(pk=pkId).exists():
            post = Post.objects.get(pk=pkId)
            serializer = serializers.PostSerializer(post)
            return Response({'status': 'success','data': serializer.data, 'msg':''})
        else:
            return Response({'status': 'error', 'data': '', 'msg': 'Invalid Post!'})
            
            
class PostSingleUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.PostSerializer
    def post(self, *args, **kwargs):
        postData = self.request.data
        pkId = postData['pk']
        if Post.objects.filter(pk=pkId).exists():
            post = Post.objects.get(pk=pkId)
            serializer = serializers.PostSerializer(post, data=postData)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data, 'msg': 'Blog Updated Successfully'})
            return Response({'status': 'error', 'data': serializer.data, 'msg': serializer.errors})
        else:
            return Response({'status': 'error', 'data': '', 'msg': 'Invalid Post!'})
            

class PostSingleDeleteView(generics.DestroyAPIView):
    serializer_class = serializers.PostSerializer
    def post(self, *args, **kwargs):
        postData = self.request.data
        pkId = postData['pk']
        if Post.objects.filter(pk=pkId).exists():
            instance = Post.objects.get(pk=pkId)
            instance.delete()
            return Response({'status': 'success','data': postData, 'msg':'Blog Deleted Successfully!'})
        else:
            return Response({'status': 'error', 'data': postData, 'msg': 'Invalid Post!'})
            
            
