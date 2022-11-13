from django.urls import path
from user import views
from user.views import RegistrUserView

urlpatterns = [
    path('register/', RegistrUserView.as_view(), name='register'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
