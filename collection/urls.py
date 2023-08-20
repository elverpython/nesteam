from rest_framework import routers
from django.urls import path, include
from .views import *



collection_router = routers.DefaultRouter()
collection_router.register(r'', CollectionViewSet)


urlpatterns = [
    path('', include(collection_router.urls)),
    path('collecfilter/', CollectionListAPIView.as_view(), name='collecfilter'),

]