import csv
from typing import List
from model import *


def parseMetaData(filepath: str) -> dict[str, int | List[int]]:
    """
    parses metadata and returns the main field size and sub field sizes
    """
    MAIN_FIELD_SIZE: float = 0
    SUB_FIELD_SIZES: List[float] = []

    with open(filepath + r"\metadata.csv", "r") as f:
        reader = csv.reader(f, skipinitialspace=True)
        next(reader)
        for i in reader:
            MAIN_FIELD_SIZE = float(i[0])
            SUB_FIELD_SIZES.append(float(i[1]))

    return {"MAIN_FIELD_SIZE": MAIN_FIELD_SIZE, "SUB_FIELD_SIZES": SUB_FIELD_SIZES}


def parseCareAreas(filepath: str) -> List[CareArea]:
    """
    parses carearea and returns the list of careareas
    """
    care_areas: List[CareArea] = []
    with open(filepath + r"\CareAreas.csv", "r") as f:
        reader = csv.reader(f, skipinitialspace=True)
        for row in reader:
            ca = CareArea(
                id=int(row[0]),
                xmin=float(row[1]),
                xmax=float(row[2]),
                ymin=float(row[3]),
                ymax=float(row[4]),
            )
            care_areas.append(ca)
    return care_areas
