from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.order_list, name='list'),
    path('create/', views.order_create, name='create'),
    path('<int:pk>/files/<int:file_id>/', views.order_file_download, name='file_download'),
    path('<int:pk>/final/', views.order_final_file_download, name='final_file_download'),
    path('<int:pk>/', views.order_detail, name='detail'),
]