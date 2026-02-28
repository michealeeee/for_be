from django.urls import path, include
from .views import CreateUserAPIView, GetUserAPIView,GetAllUserAPIView,DeleteUserAPIView,UpdateUserAPIView

urlpatterns = [
    path('user/create',CreateUserAPIView.as_view(),name="An API that creates a user"),
    path('user/get/<name>',GetUserAPIView.as_view(),name="An API that gets a user"),
    path('user/all',GetAllUserAPIView.as_view(),name="An API that gets all users"),
    path('user/delete/<name>',DeleteUserAPIView.as_view(),name="An API that delete all users"),
    path('user/update/<name>',UpdateUserAPIView.as_view(),name="An API that update all users"),
]