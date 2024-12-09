from Appliances.Appliance import Appliance
class Iron(Appliance):
    def calculate_energy_consumption(self, days):
        return self.power * self.usage_per_day * days / 1000

    def calculate_cost(self, days, cost_per_kwh):
        energy = self.calculate_energy_consumption(days)
        return energy * cost_per_kwh

    def __str__(self):
        return f'Iron: Power={self.power}W, Usage per day={self.usage_per_day} hours'

    def __repr__(self):
        return f'Iron(power={self.power}, usage_per_day={self.usage_per_day})'

