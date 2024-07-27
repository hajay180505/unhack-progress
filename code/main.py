from parse_csv import *
from logic import findMainFields, findSubFields, notCovered
from time import sleep
csv.register_dialect("d", lineterminator="\n")


# FILE_DIRECTORY = r"C:\Users\skava\Documents\GitHub\unhack-progress\src\Dataset-0\Dataset-0\1st"
FILE_DIRECTORY = r'C:\Users\skava\Documents\GitHub\unhack-progress\src\Student-Dataset-1\Dataset-1\6th'

metadata = parseMetaData(filepath=FILE_DIRECTORY)
care_areas = parseCareAreas(filepath=FILE_DIRECTORY)

mainfield_id = 0
subfield_id = 0
main_fields_all = []
for ca in care_areas:
    # print(notCovered(ca, main_fields_all))
    if notCovered(ca, main_fields_all):
        main_fields: List[MainField] = findMainFields(
            ca, metadata["MAIN_FIELD_SIZE"], mainfield_id
        )
        print(len(main_fields))
        mainfield_id += len(main_fields)
        main_fields_all.extend(main_fields)
        # print("MAIN FIELDS COUNT = ", mainfield_id + 1)
        with open(r"code\test" + r"\mainfields.csv", "a") as f:
            writer = csv.writer(f, dialect="d")
            # print("WRITTEN STUFF :", main_fields,"\n\n\n")
            # sleep(3)
            for row in main_fields:
                writer.writerow(row)

    sub_fields: List[SubField] = findSubFields(ca, metadata["SUB_FIELD_SIZES"], subfield_id)
    subfield_id += len(sub_fields)

    with open(r"code\test" + r"\subfields.csv", "a") as f:
        writer = csv.writer(f, dialect="d")
        for row in sub_fields:
            writer.writerow(row)
    print("Done writing for Care area #", ca.id)

print(
    "Successfully written both files for all careareas. Output file paths : \n\t",
    FILE_DIRECTORY + r"\mainfields.csv" + "\n\t" + FILE_DIRECTORY + r"\subfields.csv",
)

