from django.urls import path

from .views import (
    ArticleDetailView,
    ArticleListView
    )

app_name = "articles"
urlpatterns = [
    path('', ArticleListView.as_view(),name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(),name='product-detail'),

]