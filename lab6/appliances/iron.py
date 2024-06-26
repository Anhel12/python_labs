class Iron:
    def __init__(self, power, usage_per_day):
        self.power = power
        self.usage_per_day = usage_per_day

    def calculate_energy_consumption(self, days):
        return self.power * self.usage_per_day * days / 1000

    def calculate_cost(self, days, cost_per_kwh):
        energy = self.calculate_energy_consumption(days)
        return energy * cost_per_kwh
