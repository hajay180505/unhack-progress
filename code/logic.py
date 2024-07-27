from model import *
from typing import List
# from math import floor, ceil

#delete this
# from time import sleep


def isCovered(mainfield :MainField, ca : CareArea) -> bool: 
    # print( f"Lx : {ca.xmin >= mainfield.xmin} \n", 
    #         f"Rx : {ca.xmax <= mainfield.xmax} \n",  
    #         f"Ly : {ca.ymin >= mainfield.ymin} \n", 
    #         f"Ry : {ca.ymax <= mainfield.ymax} \n"
    # )

    if (
        (ca.xmin >= mainfield.xmin) and 
        (ca.xmax <= mainfield.xmax) and 
        (ca.ymin >= mainfield.ymin) and (ca.ymax <= mainfield.ymax)
    ) :
        return True
    return False

def findMainFields( ca :  CareArea, main_field_size : float, mainfield_id : int) -> List[MainField] :
    ca_width = ca.xmax - ca.xmin
    ca_height = ca.ymax - ca.ymin
    id : int = mainfield_id
    print("Care area id : ", ca.id)
    mainfields : List[MainField] = []
    xstart = ca.xmin
    ystart = ca.ymin

    while not ca.isCovered :
        mainfield = MainField(id = id,
                         xmin = xstart,
                         xmax = xstart + main_field_size,
                         ymin = ystart,
                         ymax = ystart + main_field_size
                            )
        print(f"Main field created : {mainfield}")
        mainfields.append(mainfield)
        if isCovered(mainfield, ca):
            ca.isCovered  = True
        else:
            xstart += main_field_size
            ystart += main_field_size
            id += 1
    return mainfields


def findSubFields(main_fields : List[MainField] , sub_field_sizes : List[float]) -> List[SubField] :
    ...



if __name__ == "__main__":
    from parse_csv import *

    FILE_DIRECTORY = r'C:\Users\skava\Documents\GitHub\unhack-progress\src\Dataset-0\Dataset-0\Sample\Input and Output'

    metadata = parseMetaData(filepath=FILE_DIRECTORY)
    care_areas = parseCareAreas(filepath=FILE_DIRECTORY)
    print(care_areas)
    main_fields : List[MainField] = []
    for ca in care_areas :
        main_field: List[MainField] = findMainFields(ca , metadata['MAIN_FIELD_SIZE'])
        main_fields.append(main_field)
    print(main_fields)