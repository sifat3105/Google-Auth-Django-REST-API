from django.urls import path
from .views import google_login_view, user_detail, profile_view, LogoutView, logout_view

urlpatterns = [
    path('', google_login_view, name='google-login'),
    path('accounts/profile/', profile_view, name='profile_view'),
    path('user/', user_detail),
    path('logout/', logout_view, name='logout'),
    path('api/logout/', LogoutView.as_view(), name='api-logout'),
]