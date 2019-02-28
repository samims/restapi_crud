from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from .views import CustomObtainJSONWebtoken, CustomRefreshJSONWebtoken, CustomVerifyJSONWebToken
from .serializers import CustomUserCreateSerializer

app_name = 'users'

urlpatterns = [
    path('api-token-auth/', CustomObtainJSONWebtoken.as_view(), name='token_obtain_pair'),
    path('api-token-refresh', RefreshJSONWebToken.as_view(),
         name='token_refresh'),
    path('api-token-verify/', VerifyJSONWebToken.as_view()),
]
