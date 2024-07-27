from parse_csv import *
from logic import findMainFields, findSubFields

# FILE_DIRECTORY = r'C:\Users\skava\Documents\GitHub\unhack-progress\src\Dataset-0\Dataset-0\Sample\Input and Output'
FILE_DIRECTORY = r'C:\Users\skava\Documents\GitHub\unhack-progress\src\Student-Dataset-1\Dataset-1\6th'
metadata = parseMetaData(filepath=FILE_DIRECTORY)
care_areas = parseCareAreas(filepath=FILE_DIRECTORY)
mainfield_id = 0
for ca in care_areas :
    main_fields: List[MainField] = findMainFields(ca , metadata['MAIN_FIELD_SIZE'], mainfield_id)
    # sub_fields : List[SubField] = findSubFields(main_fields, metadata['SUB_FIELD_SIZES'])
    mainfield_id += len(main_fields)
    with open(r'.\code\output'+r'\mainfields.csv','a') as f:
        csv.register_dialect('d', lineterminator='\n')
        writer = csv.writer(f, dialect='d')
        for row in main_fields:
            writer.writerow(row)
    
    # with open(FILE_DIRECTORY+r'\subfields.csv','a') as f:
    #     writer = csv.writer(f)
    #     writer.writerows(sub_fields)
    print('Done writing for Care area #' , ca.id)

print("Successfully written both files for all careareas. Output file paths : \n\t", FILE_DIRECTORY + r'\mainfields.csv' + '\n\t' + FILE_DIRECTORY+ r'\subfields.csv' )