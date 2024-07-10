from rest_framework import routers

from app.viewsets import (nsVS, wpVS, plVS, rdVS)


router = routers.DefaultRouter()

router.register(r"ns", nsVS, basename ='network-service')
router.register(r"wp", wpVS, basename='water-pipeline')
router.register(r"pl", plVS, basename='pipeline')
router.register(r"rd", rdVS, basename='road')    

urlpatterns = router.urls