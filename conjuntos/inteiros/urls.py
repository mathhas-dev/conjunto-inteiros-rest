from rest_framework import routers
from django.urls import path, include
from inteiros.endpoints import InteiroViewSet

router = routers.DefaultRouter(trailing_slash=True)
router.register('inteiros', InteiroViewSet, 'inteiros')

urlpatterns = [
    path('api/', include(router.urls))
]
