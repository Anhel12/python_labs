from abc import ABC, abstractmethod


class Appliance(ABC):
    def __init__(self, power, usage_per_day):
        self._power = power
        self._usage_per_day = usage_per_day

    @abstractmethod
    def calculate_energy_consumption(self, days):
        pass

    @abstractmethod
    def calculate_cost(self, days, cost_per_kwh):
        pass

    @property
    def power(self):
        return self._power

    @property
    def usage_per_day(self):
        return self._usage_per_day

    def __str__(self):
        return f'{self.__class__.__name__}: Power={self.power}W, Usage per day={self.usage_per_day} hours'

    def __repr__(self):
        return f'{self.__class__.__name__}(power={self.power}, usage_per_day={self.usage_per_day})'
