from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from .serializers import CustomJWTSerializer


class CustomObtainJSONWebtoken(ObtainJSONWebToken):
    serializer_class = CustomJWTSerializer


class CustomRefreshJSONWebtoken(RefreshJSONWebToken):
    serializer_class = CustomJWTSerializer


class CustomVerifyJSONWebToken(VerifyJSONWebToken):
    serializer_class = CustomJWTSerializer
