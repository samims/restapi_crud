from rest_framework.generics import ListCreateAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework_jwt.authentication
from .models import Post
from .serializers import PostSerializer


class PostListCreateAPIView(ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    # authentication_classes = []
