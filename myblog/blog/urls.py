from django.urls import path, include
from .views import post_list, post_detail, post_create, post_update, post_delete, PostViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/new/', post_create, name='post_create'), 
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('post/<slug:slug>/edit/', post_update, name='post_update'),
    path('post/<slug:slug>/delete/', post_delete, name='post_delete'),
    path('api/', include(router.urls)),
]


