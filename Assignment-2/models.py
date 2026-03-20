from abc import ABC, abstractmethod

class StationAsset(ABC):
    def __init__(self, name, price_per_unit):
        self.name = name
        self.price_per_unit = price_per_unit

        
    @abstractmethod
    def calculate_revenue(self):
        pass

    def __str__(self):
        return self.name


class FuelDispenser(StationAsset):
    """Represents fuel sales revenue."""
    def __init__(self, name, price_per_unit, litre_sold):
        super().__init__(name, price_per_unit)
        self.litre_sold = litre_sold
    

    def calculate_revenue(self):
        return self.litre_sold * self.price_per_unit
    

class CarWash(StationAsset):
    """Represents car wash service revenue."""
    def __init__(self, name, price_per_unit, cars_washed):
        super().__init__(name, price_per_unit)
        self.cars_washed = cars_washed

    
    def calculate_revenue(self):
        return self.cars_washed * self.price_per_unit
    

    