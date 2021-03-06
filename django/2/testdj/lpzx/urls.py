from django.urls import path
from lpzx import views as view
from django.conf.urls import url

from .views import (
    Detail_View,
    List_View,
    Create_View,
    Update_View,
    Delete_View,
    Date_View,
    Date_New_View,
    download
    )

app_name = "lpzx"
urlpatterns = [
    path('', List_View.as_view(),name='lpzx-list'),
    path('create/', Create_View.as_view(),name='lpzx-create'),
    path('<int:id>/', Detail_View.as_view(),name='lpzx-detail'),
    path('<int:id>/update/', Update_View.as_view(),name='lpzx-update'),
    path('<int:id>/delete/', Delete_View.as_view(),name='lpzx-delete'),
    path('date/', Date_View,name='lpzx-date'),
    path('date_view/', Date_New_View,name='lpzx-date-view'),
    url(r'^ajax_handler/$', view.ajax_handler),
    url(r'^download/',view.download,name="download"),
    url(r'^$', view.index),
    
# 
]