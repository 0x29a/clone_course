""" API v1 URLs. """
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import CloneCourse

app_name = 'v1'

router = SimpleRouter()
router.register(r'clone', CloneCourse, basename='clone')

urlpatterns = [
    path('', include(router.urls))
]