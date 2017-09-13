# Coordinates Extractor
This script aims to extract the coordinates from a Google Maps URL.

### Running
```
$ virtualenv env
$ source env/bin/activate
$(env) pip install -r pip-freeze.txt
$(env) python init.py "See me on Google Maps! https://maps.app.goo.gl/EGYoGW0WmMDbtNkD2"
```

### Result
```
https://maps.app.goo.gl/EGYoGW0WmMDbtNkD2: 37.06250000000001,-95.67706800000001
```
