from rest_framework import routers

from utilsapp.viewsets import (nsVS, wpVS, plVS, rdVS, rowVS, mhVS)


router = routers.DefaultRouter()

router.register(r"ns", nsVS, basename ='network-service')
router.register(r"wp", wpVS, basename='water-pipeline')
router.register(r"pl", plVS, basename='pipeline')
router.register(r"rd", rdVS, basename='road')
router.register(r"row", rowVS, basename='row')
router.register(r"mh", mhVS, basename='manhole')

urlpatterns = router.urls

