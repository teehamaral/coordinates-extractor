
from coordinates_extractor import CoordinatesExtractor

c = CoordinatesExtractor(text='See me on Google Maps! https://maps.app.goo.gl/EGYoGW0WmMDbtNkD2')

if c.text_check():
    print(c.get_coordinates())