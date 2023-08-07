from django.contrib import admin
from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('post_list/', views.post_list, name='post_list'), # 127.0.0.1:8000/post/
    path('detail/<int:pk>/', views.post_detail, name='post_detail'), # 127.0.0.1:8000/post/detail/1
    path('new/', views.post_new, name='post_new'), # 127.0.0.1:8000/post/new/
    path('detail/<int:pk>/modify/', views.post_modify, name='post_modify'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)