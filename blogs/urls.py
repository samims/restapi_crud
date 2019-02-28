from django.urls import path
from .views import PostListCreateAPIView

app_name = 'blogs'
urlpatterns = [
    path('list/', PostListCreateAPIView.as_view(), name='list'),

]
