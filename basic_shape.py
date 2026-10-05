from abc import ABC, abstractmethod

"The overarching class that the other shape classes will inherit from. Provides the area and name variables and their respective getters/setters for inheritance, while remaining wholly abstract"
class BasicShape(ABC):
    def __init__(self, name, area):
        self._name = name
        self._area = 0.0

    @property
    def name(self):
        return self._name

    "The setter for the name property, able to be passed down to the Basic Shape's subclasses and forced to fit(not abstract)"
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a valid string")
        self._name = value

    @property
    def area(self):
        return self._area

    @abstractmethod
    def calc_area(self):
        pass
