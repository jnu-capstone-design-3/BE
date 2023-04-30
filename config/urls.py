from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls),
    # re_path(r'^accounts/registration/confirm-email/(?P<key>.+)/$', confirm_email, name='confirm_email'),
    path('accounts/', include('account.urls')),
    path('navi/', include('navigation.urls')),    
]