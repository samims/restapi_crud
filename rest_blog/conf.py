# from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_payload_handler


def jwt_custom_payload_handler(user):
    payload = jwt_payload_handler(user)
    payload['email'] = user.email
    payload['username'] = user.email
