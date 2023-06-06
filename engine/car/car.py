from abc import ABC, abstractmethod
class Car(ABC):
    def __int__(self, Engine, Battery):
        self.Engine = Engine
        self.Battery = Battery
    @abstractmethod
    def needs_service(self):
        pass
        #return self.Battery.needs_service or self.Engine.needs_service()