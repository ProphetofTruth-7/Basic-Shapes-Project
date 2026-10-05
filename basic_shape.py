from abc import ABC, abstractmethod

class BasicShape(ABC):
    def __init__(self, name, area):
        self._name = name
        self._area = area

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Name must be a valid string")
        self._name = value
