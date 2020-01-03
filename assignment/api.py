from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'filesAPI', views.FileViewSet)