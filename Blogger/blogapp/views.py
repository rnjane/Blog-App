from rest_framework import views, permissions, response, status, generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from . import serializers, models

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
            token, _ = Token.objects.get_or_create(user=user)
            return response.Response({'token': token.key},
                    status=status.HTTP_200_OK)


class CategoriesCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.CategoriesSerializer
    queryset = models.Categories.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class CategoryEditDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.CategoriesSerializer
    queryset = models.Categories.objects.all()


class ArticleCreate(generics.CreateAPIView):
    serializer_class = serializers.ArticlesSerializer
    queryset = models.Articles.objects.all()

    def perform_create(self, serializer):
        serializer.save(writer=self.request.user)

class ArticlesList(generics.ListAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = serializers.ArticlesSerializer
    queryset = models.Articles.objects.all()