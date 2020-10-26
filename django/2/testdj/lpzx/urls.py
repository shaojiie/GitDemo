from django.urls import path

from .views import (
    Detail_View,
    List_View
    )

app_name = "lpzx"
urlpatterns = [
    path('', List_View.as_view(),name='lpzx-list'),
    path('<int:id>/', Detail_View.as_view(),name='product-detail'),

]