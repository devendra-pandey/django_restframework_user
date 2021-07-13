from .views import RegisterAPI
from django.urls import path , include
from knox import views as knox_views
from .views import LoginAPI , ChangePasswordView, All_user




urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('all_user/', All_user.as_view())

]