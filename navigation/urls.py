from django.urls import path
from .views import Index

urlpatterns = [
    path('test/', Index.as_view(), name='test'),
]