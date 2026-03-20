from models import FuelDispenser, CarWash

# create objects
fuel_dispenser = FuelDispenser("Fuel Dispenser", 50, 60)
car_wash = CarWash("Car Wash", 20, 3)

# store in list
assets = [fuel_dispenser, car_wash]

# calculate total revenue
total_revenue = 0

for asset in assets:
    total_revenue += asset.calculate_revenue()

print("Total Revenue:", total_revenue)