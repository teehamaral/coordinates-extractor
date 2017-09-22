# Coordinates Extractor
This script aims to extract the coordinates from a Google Maps URL or VCF file (Apple sharing).

### Install
```
$ cd /your/project/path/
$ virtualenv env
$ source env/bin/activate
$(env) pip install git+https://github.com/codenonprofits/coordinates-extractor.git
```

### Usage
```
from coordinates_extractor import CoordinatesExtractor

# From a Google URL
coordinates = CoordinatesExtractor(text="See me on Google Maps! https://maps.app.goo.gl/EGYoGW0WmMDbtNkD2")

# Check if there's Google Maps URL
coordinates.text_check()

# Get coordinates
(lat, long) = coordinates.get_coordinates()


# From a VCF file (Apple sharing)
c = CoordinatesExtractor(file_path='/path/to/your/file.vcf')

(lat, long) = c.get_coordinates_from_file()

```
