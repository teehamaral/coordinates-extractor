# Coordinates Extractor
This script aims to extract the coordinates from a Google Maps URL.

### Install
```
$ cd /your/project/path/
$ virtualenv env
$ source env/bin/activate
$(env) pip install git+https://github.com/codenonprofits/coordinates-extractor.git@change-to-lib
```

### Usage
```
coordinates = CoordinatesExtractor(text="See me on Google Maps! https://maps.app.goo.gl/EGYoGW0WmMDbtNkD2")

# Check if there's Google Maps URL
coordinates.text_check()

# Get coordinates
(lat, long) = coordinates.get_coordinates()
```
