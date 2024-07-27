from model import *
from typing import List
from math import floor, ceil
from shapely.geometry import Polygon

# delete this
# from time import sleep


def isCovered(mainfield: MainField, ca: CareArea) -> bool:
    # print( f"Lx : {ca.xmin >= mainfield.xmin} \n",
    #         f"Rx : {ca.xmax <= mainfield.xmax} \n",
    #         f"Ly : {ca.ymin >= mainfield.ymin} \n",
    #         f"Ry : {ca.ymax <= mainfield.ymax} \n"
    # )

    if (
        (ca.xmin >= mainfield.xmin)
        and (ca.xmax <= mainfield.xmax)
        and (ca.ymin >= mainfield.ymin)
        and (ca.ymax <= mainfield.ymax)
    ):
        return True
    return False


def findMainFields(
    ca: CareArea, main_field_size: float, mainfield_id: int
) -> List[MainField]:

    id: int = mainfield_id
    print("Care area id : ", ca.id)
    mainfields: List[MainField] = []
    xstart = ca.xmin
    ystart = ca.ymin

    while not ca.isCovered:
        mainfield = MainField(
            id=id,
            xmin=xstart,
            xmax=xstart + main_field_size,
            ymin=ystart,
            ymax=ystart + main_field_size,
        )
        print(f"Main field created : {mainfield}")
        mainfields.append(mainfield)
        if isCovered(mainfield, ca):
            ca.isCovered = True
            ca.mainFieldId = id
        # else:
        #     xstart += main_field_size
        #     ystart += main_field_size
        #     id += 1
    return mainfields


def findSubFields(
    ca: CareArea, sub_field_sizes: List[float], id: int
) -> List[SubField]:
    ca_width = ca.xmax - ca.xmin
    ca_height = ca.ymax - ca.ymin

    if len(sub_field_sizes) != 1:
        return NotImplementedError("Yet to implement")

    subfields: List[SubField] = []

    sf_per_row = ceil(ca_width / sub_field_sizes[0])
    rows = ceil(ca_height / sub_field_sizes[0])

    xstart = ca.xmin
    ystart = ca.ymin
    yend = ca.ymin + sub_field_sizes[0]

    for j in range(rows):
        for i in range(sf_per_row):
            sf = SubField(
                id=id,
                mainFieldId=ca.mainFieldId,
                xmin=xstart,
                xmax=xstart + sub_field_sizes[0],
                ymin=ystart,
                ymax=yend,
            )
            xstart += sub_field_sizes[0]
            subfields.append(sf)
            id += 1
        ystart += sub_field_sizes[0]
        yend += sub_field_sizes[0]
        xstart = ca.xmin


    return subfields

def notCovered(ca : CareArea , mfs :List[MainField]) -> bool:
    if mfs:
        total_intersection = sum( [ca.toPolygon().intersection(x.toPolygon()).area for x in mfs ])
        for mf in mfs:
            # print(ca.toPolygon().is_valid)
            # print(mf.toPolygon().is_valid)
            if (ca.toPolygon().intersection(mf.toPolygon()).area != ca.toPolygon().area) or (total_intersection == ca.toPolygon().area) :
                return False
        return True
    return True

    # if mfs:
    #     print(f"bound xmin ={min([x.xmin for x in mfs])}",
    #                   f"xmax = {max([x.xmax for x in mfs])}",
    #                   f"ymin = {min([x.ymin for x in mfs])}",
    #                   f"ymax = {max([x.ymax for x in mfs])}"
    #            )
    #     main_field_bound = MainField(
    #         id= -1,
    #         xmin = min([x.xmin for x in mfs]),
    #         xmax = max([x.xmax for x in mfs]),
    #         ymin = min([x.ymin for x in mfs]),
    #         ymax = max([x.ymax for x in mfs]),
    #     )
    #     print(main_field_bound)
    #     return not isCovered(main_field_bound, ca) 
    # else: return True



if __name__ == "__main__":
    from parse_csv import *

    FILE_DIRECTORY = r"C:\Users\skava\Documents\GitHub\unhack-progress\src\Dataset-0\Dataset-0\Sample\Input and Output"

    metadata = parseMetaData(filepath=FILE_DIRECTORY)
    care_areas = parseCareAreas(filepath=FILE_DIRECTORY)
    print(care_areas)
    main_fields: List[MainField] = []
    for ca in care_areas:
        main_field: List[MainField] = findMainFields(ca, metadata["MAIN_FIELD_SIZE"])
        main_fields.append(main_field)
    print(main_fields)
