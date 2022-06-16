import os
import sys
import logging
import glob
from dotenv import load_dotenv
import requests
from zipfile import ZipFile


from shapely.geometry import mapping, shape
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
        return glob.glob("data/*.shp")[0]
    except IndexError as e:
        logger.error(f"could not find shapefile: {e}")
        sys.exit()

def build():
    fpath_shapefile = get_shapefile_fpath()
    logger.info(f"building shapely file using {fpath_shapefile}")
    

if __name__ == "__main__":
    get_shapefiles()
    extract_shapefiles()
    build()
