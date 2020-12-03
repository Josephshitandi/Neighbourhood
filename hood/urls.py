from django.urls import path,re_path,include
from .views import NeighbourhoodViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Neighbourhood',NeighbourhoodViewSet)

urlpatterns = [
    path("", include(router.urls) ),
]