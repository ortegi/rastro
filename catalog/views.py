from typing import Any
from django.shortcuts import render
from .models import Article, Category
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArticleSerializer, CategorySerializer
from .models import Article, Category
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action

"""def index(request):

    num_articles = Article.objects.all().count()
    num_categories = Category.objects.all().count()
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits
    
    context = {
        'num_articles': num_articles,
        'num_categories': num_categories,
        'num_visits': num_visits,
    }
    
    return render(request, 'index.html', context)



class ArticleListView(generic.ListView):
    model = Article
    paginate_by = 3
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_categories"] = Category.objects.all() 
        return context
        """
    
    
"""class ArticleDetailView(generic.DetailView):
    model = Article"""
    
    
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    
    @action(detail=False, methods=['get'], url_path='by-category/(?P<category_id>[^/.]+)')
    def by_category(self, request, category_id=None):
        
        if(category_id is None):
           return Response({"detail": "Category id is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        
        articles = Article.objects.filter(category__id=category_id)
        
        if not articles.exists():
            return Response({"detail": "No articles Found in this category"}, status=status.HTTP_404_NOT_FOUND)
            
        
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'], url_path='query/(?P<query>[^/.]+)')
    def query(self, request, query=None):
        
        if query is None:
            return Response({"detail": "Query is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        articles = Article.objects.filter(title__icontains=query)
        
        if not articles.exists():
            return Response({"detail": "No articles Found with this query"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)



class Category_APIView(APIView):
    
    def get(self, request, format=None, *args ,**kwargs): 
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    
    


