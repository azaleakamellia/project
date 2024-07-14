'''
The load.py file is meant to upload only one shapefile at a time. Thus, it is best that you either create it separately or upload them one by one by using the same load.py
file and commenting out majority of the data and leaving just one to run; one at a time. 
'''

from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from utilsapp.models import (mh)

'''
ns_mapping = {
    'type': 'TYPE',
    'client_gov': 'CLIENT_GOV',
    'handle': 'Handle',
    'layer': 'Layer',s
    'lyrhandle': 'LyrHandle',
    'elevation': 'Elevation',
    'refname': 'RefName',
    'docname': 'DocName',
    'docpath': 'DocPath',
    'doctype': 'DocType',
    'docver': 'DocVer',
    'docupdate': 'DocUpdate',
    'globalwidt': 'GlobalWidt',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING',
}

ns_shp = Path(__file__).resolve().parent / 'data' / 'network_service.shp'

def run(verbose=True):
    lm = LayerMapping(ns, ns_shp, ns_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)



# Water Pipeline
wp_mapping = {
    'type': 'TYPE',
    'client_gov': 'CLIENT_GOV',
    'handle': 'Handle',
    'layer': 'Layer',
    'lyrhandle': 'LyrHandle',
    'elevation': 'Elevation',
    'refname': 'RefName',
    'docname': 'DocName',
    'doctype': 'DocType',
    'docver': 'DocVer',
    'docupdate': 'DocUpdate',
    'globalwidt': 'GlobalWidt',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING25D',
}

wp_shp = Path(__file__).resolve().parent / 'data' / 'water_pipeline.shp'

def run(verbose=True):
    lm = LayerMapping(wp, wp_shp, wp_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)



#Powerline
pl_mapping = {
    'type': 'TYPE',
    'client_gov': 'CLIENT_GOV',
    'handle': 'Handle',
    'layer': 'Layer',
    'lyrhandle': 'LyrHandle',
    'elevation': 'Elevation',
    'refname': 'RefName',
    'docname': 'DocName',
    'doctype': 'DocType',
    'docver': 'DocVer',
    'docupdate': 'DocUpdate',
    'globalwidt': 'GlobalWidt',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING25D',
}

pl_shp = Path(__file__).resolve().parent / 'data' / 'powerline.shp'

def run(verbose=True):
    lm = LayerMapping(pl, pl_shp, pl_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


#Roads
rd_mapping = {
    'type': 'TYPE',
    'client_gov': 'CLIENT_GOV',
    'handle': 'Handle',
    'layer': 'Layer',
    'lyrhandle': 'LyrHandle',
    'elevation': 'Elevation',
    'name': 'Name',
    'docname': 'DocName',
    'doctype': 'DocType',
    'docver': 'DocVer',
    'docupdate': 'DocUpdate',
    'globalwidt': 'GlobalWidt',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING25D',
}

rd_shp = Path(__file__).resolve().parent / 'data' / 'road.shp'

def run(verbose=True):
    lm = LayerMapping(rd, rd_shp, rd_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)

    

#Row
row_mapping = {
    'type': 'TYPE',
    'client_gov': 'CLIENT_GOV',
    'entity': 'Entity',
    'handle': 'Handle',
    'layer': 'Layer',
    'lyrfrzn': 'LyrFrzn',
    'lyron': 'LyrOn',
    'color': 'Color',
    'linetype': 'Linetype',
    'elevation': 'Elevation',
    'linewt': 'LineWt',
    'refname': 'RefName',
    'docupdate': 'DocUpdate',
    'docid': 'DocId',
    'globalwidt': 'GlobalWidt',
    'name': 'NAME',
    'length': 'LENGTH',
    'enclosed_a': 'ENCLOSED_A',
    'bearing': 'BEARING',
    'shape_leng': 'Shape_Leng',
    'geom': 'MULTILINESTRING25D',
}

row_shp = Path(__file__).resolve().parent / 'data' / 'row.shp'

def run(verbose=True):
    lm = LayerMapping(row, row_shp, row_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)



'''


mh_mapping = {
    'entity': 'Entity',
    'handle': 'Handle',
    'layer': 'Layer',
    'lyrfrzn': 'LyrFrzn',
    'lyron': 'LyrOn',
    'color': 'Color',
    'linetype': 'Linetype',
    'elevation': 'Elevation',
    'linewt': 'LineWt',
    'refname': 'RefName',
    'docupdate': 'DocUpdate',
    'docid': 'DocId',
    'globalwidt': 'GlobalWidt',
    'name': 'NAME',
    'length': 'LENGTH',
    'enclosed_a': 'ENCLOSED_A',
    'bearing': 'BEARING',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON25D',
}

mh_shp = Path(__file__).resolve().parent / 'data' / 'manhole.shp'

def run(verbose=True):
    lm = LayerMapping(mh, mh_shp, mh_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
