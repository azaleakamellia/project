'''
The load.py file is meant to upload only one shapefile at a time. Thus, it is best that you either create it separately or upload them one by one by using the same load.py
file and commenting out majority of the data and leaving just one to run; one at a time. 
'''

from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from app.models import rd

'''
ns_mapping = {
    'type': 'TYPE',
    'client_gov': 'CLIENT_GOV',
    'handle': 'Handle',
    'layer': 'Layer',
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

'''

#Roads
rd_mapping = {
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

rd_shp = Path(__file__).resolve().parent / 'data' / 'road.shp'

def run(verbose=True):
    lm = LayerMapping(rd, rd_shp, rd_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


''' 
#Lots
lot_mapping = {
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
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON25D',
}

lot_shp = Path(__file__).resolve().parent / 'data' / 'lot.shp'

def run(verbose=True):
    lm = LayerMapping(lot, lot_shp, lot_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)


'''

