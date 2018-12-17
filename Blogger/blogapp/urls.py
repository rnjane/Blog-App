from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),

    #categories related urls
    path('category/', views.CategoriesCreateView.as_view(), name='create_category'), #this url covers for creating and viewing all categories
    path('category/<int:pk>/', views.CategoryEditDelete.as_view(), name='category'), #this url covers for edit, delete and view single category

    #articles related urls
    path('create-article/', views.ArticleCreate.as_view(), name='create_article'),
    path('articles/', views.ArticlesList.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticleEditDeleteView.as_view(), name='article') #this url covers for edit, delete and view single article
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)