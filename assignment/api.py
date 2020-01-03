from rest_framework import routers
from myapp import views

# For routing REST requests
router = routers.DefaultRouter()
router.register(r'filesAPI', views.FileViewSet)