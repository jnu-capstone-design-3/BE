from django.urls import path, include #, re_path
# from allauth.account.views import confirm_email
from account import views

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    # re_path(r'^accounts/registration/confirm-email/(?P<key>.+)/$', confirm_email, name='confirm_email'),
    # path('social/', include('allauth.urls')),
    path('social/kakao/login/', views.kakao_login, name='kakao_login'),
    path('social/kakao/callback/', views.kakao_callback, name='kakao_callback'),
    path('social/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
]