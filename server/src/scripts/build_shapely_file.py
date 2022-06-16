import os
import sys
import logging
import glob
import pickle
from dotenv import load_dotenv
import requests
from zipfile import ZipFile
from shapely.geometry import shape, GeometryCollection
import fiona

LGA_ZIPFILE_LOCATION="data/lga_shapefile.zip"

load_dotenv()
logging.basicConfig(level=os.environ.get("LOGGING_LEVEL", "INFO"))
logger = logging.getLogger(__name__)

def get_shapefiles():
    try:
        logger.info("downloading LGA shapefile")
        shapefile_url = os.environ["LGA_SHAPEFILE_URL"]
        response = requests.get(shapefile_url)
        assert response.status_code == 200
    except AssertionError:
        logger.error("error downloading lga shapefile")
        sys.exit()

    open(LGA_ZIPFILE_LOCATION, "wb").write(response.content)

def extract_shapefiles():
    logger.info("extracting shapefiles")
    with ZipFile(LGA_ZIPFILE_LOCATION, 'r') as f:
        f.extractall("data")

def get_shapefile_fpath():
    try:
        return glob.glob("data/LGA_*.shp")[0]
    except IndexError as e:
        logger.error(f"could not find shapefile: {e}")
        sys.exit()

def get_lga_name(lga):
    try:
        lga_props = lga["properties"]
        return [lga_props[x] for x in lga_props if "LGA_NAME" in x].pop()
    except KeyError as e:
        logger.info(f"Key missing from LGA: {e}")
    except IndexError as e:
        logger.info(f"LGA name missing: {e}")
    sys.exit()

def build():
    fpath_shapefile = get_shapefile_fpath()
    logger.info(f"building shapely file using {fpath_shapefile}")
    
    shapely_file_dict = {}

    with fiona.open(fpath_shapefile, 'r') as source:
        for i, lga in enumerate(source):
            logger.info(f"Processing LGA at index {i}")
            lga_name = get_lga_name(lga)
            try:
                lga_geoms = lga["geometry"]
                assert lga_geoms is not None
            except KeyError as e:
                logging.info(f"LGA {lga_name} has no geometry")
                continue
            except AssertionError:
                logging.info(f"LGA {lga_name} geometry is None")
                continue
            
            shapes = shape(lga_geoms)
            shapely_file_dict[lga_name] = GeometryCollection([shapes]) 

    with open("data/lga_shapely.pickle", "wb") as f:
        pickle.dump(shapely_file_dict,f)
               
def find(lat, lon):
    from shapely.geometry import Point
    point = Point(lat, lon)
    with fiona.open("data/lga_shapely.shp", "r") as f:
        for lga in f:
            lga_name = get_lga_name(lga)
            # print(lga["geometry"].keys())
            # print(type(lga["geometry"]["coordinates"]))
            # print(type(shape(lga["geometry"])))
            # return

if __name__ == "__main__":
    get_shapefiles()
    extract_shapefiles()
    build()
