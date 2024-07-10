from rest_framework import viewsets
from rest_framework_gis import filters

from app.models import (ns, wp, pl, rd)
from app.serializers import (nsSerializer, wpSerializer, plSerializer, rdSerializer)


class nsVS(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = 'geom'
    filter_backends = (filters.InBBOXFilter,
                       )
    queryset = ns.objects.all()
    serializer_class = nsSerializer


class wpVS(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = 'geom'
    filter_backends = (filters.InBBOXFilter,
                       )
    queryset = wp.objects.all()
    serializer_class = wpSerializer


class plVS(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = 'geom'
    filter_backends = (filters.InBBOXFilter,
                       )
    queryset = pl.objects.all()
    serializer_class = plSerializer


class rdVS(viewsets.ReadOnlyModelViewSet):
    bbox_filter_field = 'geom'
    filter_backends = (filters.InBBOXFilter,
                       )
    queryset = rd.objects.all()
    serializer_class = rdSerializer