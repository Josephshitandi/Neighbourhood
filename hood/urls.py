
from rest_framework.routers import DefaultRouter
from django.urls import path,re_path,include

from .views import home, NeighbourhoodViewSet,ProfileViewSet,BusinessViewSet,PostViewSet



router = DefaultRouter()
router.register(r'Neighborhood', NeighbourhoodViewSet)
router.register(r'Profile', ProfileViewSet)
router.register(r'Business', BusinessViewSet)
router.register(r'Post', PostViewSet)

urlpatterns =[
    path("", include(router.urls) )
] 


