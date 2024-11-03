from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = [
   path('api/', include(router.urls)),
   path('api/categories', Category_APIView.as_view(), name='categories-api'),
]
