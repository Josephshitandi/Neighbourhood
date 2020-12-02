
from rest_framework.routers import DefaultRouter
from django.urls import path,re_path,include

from .views import home, NeighbourhoodViewSet,ProfileViewSet,BusinessViewSet,PostViewSet

# snippet_list = NeighbourhoodViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = NeighbourhoodViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# urlpatterns = format_suffix_patterns([
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
# ])


router = DefaultRouter()
router2 = DefaultRouter()
router3 = DefaultRouter()
router1 = DefaultRouter()
router.register(r'Neighborhood', NeighbourhoodViewSet)
router2.register(r'Profile', ProfileViewSet)
router3.register(r'Business', BusinessViewSet)
router1.register(r'Post', PostViewSet)

urlpatterns =[
    path("", include(router.urls) ),
    path("profile/", include(router2.urls) ),
    path("business/", include(router3.urls) ),
    path("post/", include(router1.urls) ),
] 

# + router.urls

# from django.urls import path
# from some_app.views import AboutView

# urlpatterns = [
#     path('about/', AboutView.as_view()),
# ]
