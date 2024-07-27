from dataclasses import dataclass


@dataclass
class MainField:
    id : int
    xmin : float
    xmax : float
    ymin : float
    ymax :float

    def __iter__(self):
        return iter( [self.id, self.xmin, self.xmax, self.ymin, self.ymax] )

@dataclass
class SubField:
    id : int
    mainFieldId : int
    xmin : float
    xmax : float
    ymin : float
    ymax : float

    def __iter__(self):
        return iter( [self.id, self.xmin, self.xmax, self.ymin, self.ymax, self.mainFieldId] )

@dataclass
class CareArea:
    id : int
    xmin : float
    xmax : float
    ymin : float
    ymax :float
