import os
import logging
from dotenv import load_dotenv

from shapely.geometry import mapping, shape
import fiona

load_dotenv()
logging.basicConfig(level=os.environ.get("LOGGING_LEVEL", "INFO"))
logger = logging.getLogger(__name__)

def build():
    logger.info("building shapely file")
    pass
    

if __name__ == "__main__":
    build()
