from rest_framework import views, permissions, response, status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

class LoginUser(views.APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return response.Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return response.Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_401_UNAUTHORIZED)
        else:
            token = Token.objects.create(user=user)
            return response.Response({'token': token.key},
                    status=status.HTTP_200_OK)