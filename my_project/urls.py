
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tweet/', views.create_tweet),
    path('api/comment/', views.create_comment),
    path('api/mark/', views.create_mark),
]
