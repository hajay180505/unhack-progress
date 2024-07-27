from parse_csv import *

FILE_DIRECTORY = r'C:\Users\skava\Documents\GitHub\unhack-progress\src\Dataset-0\Dataset-0\Sample\Input and Output'

metadata = parseMetaData(filepath=FILE_DIRECTORY)
care_areas = parseCareAreas(filepath=FILE_DIRECTORY)

print(metadata)
print(care_areas)