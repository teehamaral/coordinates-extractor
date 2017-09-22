
from coordinates_extractor import CoordinatesExtractor

c = CoordinatesExtractor(file_path='/path/to/your/file.vcf')

print(c.get_coordinates_from_file())