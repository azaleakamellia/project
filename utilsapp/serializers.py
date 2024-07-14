from rest_framework_gis import serializers

from utilsapp.models import (ns, wp, pl, rd, row, mh)

class nsSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields = ('id', 'client_gov', 'layer', 'elevation', 
                    'docupdate')
        geo_field = 'geom'
        model = ns


class wpSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields =  ('id', 'client_gov', 'layer', 'elevation', 
                    'docupdate')
        geo_field = 'geom'
        model = wp


class plSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields =  ('id', 'client_gov', 'layer', 'elevation', 
                    'docupdate')
        geo_field = 'geom'
        model = pl


class rdSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields =  ('id', 'client_gov', 'layer', 'elevation', 
                    'docupdate')
        geo_field = 'geom'
        model = rd


class rowSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields =  ('id', 'client_gov', 'layer', 'elevation', 
                    'docupdate')
        geo_field = 'geom'
        model = row

class mhSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        fields =  ('id', 'client_gov', 'layer', 'elevation', 
                    'docupdate')
        geo_field = 'geom'
        model = mh




