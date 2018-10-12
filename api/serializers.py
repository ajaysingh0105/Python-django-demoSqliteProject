# blog/serializers.py
from rest_framework import serializers
from blog.models import Post, Category
from django.contrib.auth.models import User
from django.conf import settings
from urllib.parse import urljoin

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email', 'username', 'first_name', 'last_name', 'groups')
        read_only_fields=('id','email', 'username', 'first_name', 'last_name', 'groups')

        
class CategorySerializer(serializers.ModelSerializer):
    category_slug = serializers.SerializerMethodField()
    class Meta:
        model = Category
        #fields = '__all__'
        fields = ('id','title', 'text', 'slug', 'category_slug')
        read_only_fields=('cid','title', 'text', 'status')
        
    def get_category_slug(self, category):
        slug_url = 'blog/category/'+category.slug
        url = urljoin(settings.BASE_URL, slug_url)
        return url    
        
        
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True,required=False)
    category = CategorySerializer(read_only=True,required=False)
    full_url = serializers.SerializerMethodField(read_only=True,required=False)
    post_slug = serializers.SerializerMethodField(read_only=True,required=False)
    
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'slug', 'post_slug','category', 'status', 'featured_image', 'full_url', 'author', 'created_date', 'published_date')
        read_only_fields = ('id','created_at','updated_at')
    
    def create(self, validated_data):
        return Post.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.author = validated_data.get('author', instance.author)
        instance.featured_image = validated_data.get('featured_image', instance.featured_image)
        instance.save()
        return instance
        
    def get_full_url(self, post):
        photo_url = post.featured_image.url
        url = urljoin(settings.BASE_URL, photo_url)
        return url
        
    def get_post_slug(self, post):
        slug_url = 'blog/'+post.slug
        url = urljoin(settings.BASE_URL, slug_url)
        return url