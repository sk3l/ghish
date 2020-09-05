from abc import ABC


class GhishEntity(ABC):

    def from_json(self):
        pass

    def to_cvs(self):
        pass

    def to_json(self):
        pass

    def __str__(self):
        pass
