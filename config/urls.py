from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('', include('navigation.urls')),    
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
]