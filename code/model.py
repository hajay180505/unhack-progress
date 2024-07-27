from dataclasses import dataclass
from shapely.geometry import Polygon
@dataclass
class MainField:
    id: int
    xmin: float
    xmax: float
    ymin: float
    ymax: float

    def __iter__(self):
        return iter([self.id, self.xmin, self.xmax, self.ymin, self.ymax])

    def toPolygon(self) -> Polygon:
        return Polygon(
            [(self.xmin, self.ymin),(self.xmin, self.ymax),(self.xmax, self.ymax),(self.xmax, self.ymin)]
        )
    
@dataclass
class SubField:
    id: int
    mainFieldId: int
    xmin: float
    xmax: float
    ymin: float
    ymax: float

    def __iter__(self):
        return iter(
            [self.id, self.xmin, self.xmax, self.ymin, self.ymax, self.mainFieldId]
        )


@dataclass
class CareArea:
    id: int
    xmin: float
    xmax: float
    ymin: float
    ymax: float
    mainFieldId: int = -1
    isCovered: bool = False

    def toPolygon(self) -> Polygon:
        return Polygon(
            [(self.xmin, self.ymin),(self.xmin, self.ymax),(self.xmax, self.ymax),(self.xmax, self.ymin)]
        )
