import pickle
from shapely.geometry import Point

def find_lga(lat, lon):
    point = Point(lon, lat)
    with open("data/lga_shapely.pickle", "rb") as f:
        lga_dict = pickle.load(f)
        for lga, geoms in lga_dict.items():
            if geoms.contains(point):
                return lga
        return "ERROR_UNDEFINED"
