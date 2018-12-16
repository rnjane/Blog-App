from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),

    #categories related urls
    path('create-category/', views.CategoriesCreateView.as_view(), name='create_category'),
    path('category-detail/<int:pk>/', views.CategoryEditDelete.as_view(), name='category_details'),

    #articles related urls
    path('create-article/', views.ArticleCreate.as_view(), name='create_article'),
    path('view-articles/', views.ArticlesList.as_view(), name='articles'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)