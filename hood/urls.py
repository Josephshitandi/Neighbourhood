
from rest_framework.routers import DefaultRouter
from django.urls import path,re_path,include

from .views import home, NeighbourhoodViewSet

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
router.register(r'Neighborhood', NeighbourhoodViewSet)

urlpatterns =[
    path("", include(router.urls) )
] 

# + router.urls

# from django.urls import path
# from some_app.views import AboutView

# urlpatterns = [
#     path('about/', AboutView.as_view()),
# ]
