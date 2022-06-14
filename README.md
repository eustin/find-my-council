# find-my-council
Find your Local Government Area given the your geocoded address

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

