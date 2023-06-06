from abc import ABC, abstractclassmethod

class Battery(ABC):
    @abstractclassmethod
    def needs_service(self):
        pass