# find-my-council
Find your Local Government Area given the your geocoded address

## Prerequisites

* Python 3.x
* If working on Ubuntu/Debian, you have `python3-venv` globally intalled. If not, intall it using `sudo apt install python3-venv`
* Node.js v16 and npm
* Bash

I will eventually Dockerise so that you can avoid the above hassle. 

## Current state of the project

What's currently available is functionality to map `(latitude, longitude)` pairs to LGA names. To see this in action do thes things:

* In the project's root directory, issue `make install`. This will download the LGA shapefiles from the Australian Bureau of Statistics and process them into a format suitable for use with Shapely. 
* Run `make example` to find out which LGAs some landmarks are located in!

## The Geocoding API

To map an address to a latitude and longitude coordinate pair, we will use the free service kindly provided by https://geocode.localfocus.nl/.

We will be making GET requests of the form  `https://geocode.localfocus.nl/geocode.php?boundary=AUS&q= + some URL encoded address string`.

### Example: find the coordinates of a pub near the center of Australia

Say that we want to recover the coordinates for the "Gap View Hotel" with the address `123 Gap Road, Northen Teritory, Australia`. We will make this request:

```https://geocode.localfocus.nl/geocode.php?boundary=AUS&q=123%20gap%20road%2C%20NT```

The response looks like this: 

```
[
  {
    "id": "au/countrywide:0aa6b40501b01fa4",
    "label": "123 Gap Road, Ross, NT, Australia",
    "lat": -23.721798,
    "lng": 133.869444,
    "zoom": null,
    "bbox": null,
    "type": "123 Gap Road, Ross, NT, Australia",
    "confidence": 1
  }
]
```

