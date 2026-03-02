class Vehicle:
    def __init__(self, brand, max_speed, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        self.max_speed = max_speed
    
    def description(self):
        return f"Vehicle {self.brand}, max speed: {self.max_speed} km/h"

class ElectricVehicle(Vehicle):
    def __init__(self, brand, max_speed, range_km, **kwargs):
        super().__init__(brand, max_speed, **kwargs)
        self.range_km = range_km
    
    def description(self):
        return f"{super().description()} | Electric, range: {self.range_km} km"

class ConnectedVehicle(Vehicle):
    def __init__(self, brand, max_speed, os_system, **kwargs):
        super().__init__(brand, max_speed, **kwargs)
        self.os_system = os_system
    
    def description(self):
        return f"{super().description()} | Connected, OS: {self.os_system}"

class ConnectedElectricCar(ElectricVehicle, ConnectedVehicle):
    def __init__(self, brand, max_speed, range_km, os_system):
        super().__init__(brand, max_speed, range_km, os_system=os_system)
    
    def description(self):
        return f"{super().description()} | Electric & Connected"

print("\n" + "="*50)
print("EXERCISE 4 - Connected Vehicles")
print("="*50)

tesla = ConnectedElectricCar("Tesla", 250, 500, "Tesla OS")
print(tesla.description())

print("\nMRO of ConnectedElectricCar:")
for class_name in ConnectedElectricCar.__mro__:
    print(f"  {class_name.__name__}")
