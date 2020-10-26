from django.urls import path

from .views import (
    Detail_View,
    List_View,
    Create_View,
    Update_View,
    Delete_View
    )
Update_View
app_name = "lpzx"
urlpatterns = [
    path('', List_View.as_view(),name='lpzx-list'),
    path('create/', Create_View.as_view(),name='lpzx-create'),
    path('<int:id>/', Detail_View.as_view(),name='lpzx-detail'),
    path('<int:id>/update/', Update_View.as_view(),name='lpzx-update'),
    path('<int:id>/delete/', Delete_View.as_view(),name='lpzx-delete'),
# 
]