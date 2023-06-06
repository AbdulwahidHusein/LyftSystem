from datetime import datetime
from engine.car import Car
from engine.capulet_engine import CapuletEngine


class Calliope(Car):
    def __init__(self):
        self.Engine = CapuletEngine
    def needs_service(self):
        return self.Battery.needs_service or self.Engine.needs_service()
        '''service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False'''
