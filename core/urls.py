
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstadoViewSet, CidadeViewSet
from .views_auth import SignupViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'signup', SignupViewSet, basename='signup')


urlpatterns = [
    path('', include(router.urls)),
]
