import os
import sys
from pathlib import Path

src_root = Path(os.getcwd()) / "src"
sys.path.append(src_root.as_posix())

from find_lga import find_lga

EXAMPLE_COORDS = {
    "Gap View Hotel": (-23.721798, 133.869444),
    "Berry Donut Van": (-34.7750517,150.6926413),
    "Cradle Mountain": (-41.7257949,145.3618011),
    "Luna Park, Sydney": (-33.8482061,151.210858),
    "The White House, Washington DC, USA": (38.8989302,-77.0414407),
    "Santa Apolonia Metro Station, Lisbon, Portugal": (38.7140887,-9.1268516)
}

if __name__ == "__main__":

    for landmark, coords in EXAMPLE_COORDS.items():
        print(f"{landmark} is located in {find_lga(*coords)} LGA")
