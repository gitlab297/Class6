class Vehicle:
    vehicle_type = None

class Car:
    price = 1000000

    def horse_powers(self):
        return 100


class Nissan(Vehicle, Car):
    price = 2500000


Nissan.horse = 250
Nissan.vehicle_type = 'Sedan'

print('Машина Nissan цена {} мощность {} тип {}'.format(Nissan.price, Nissan.horse, Nissan.vehicle_type))
