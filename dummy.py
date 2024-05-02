def Calculate_fare(Vehicle_type):
    distance = 10
    fare_per_km = {
        'car':30,
        'bike':20,
        'cng':25
    }
    return distance*fare_per_km.get(Vehicle_type.lower())
    

new_calculate = Calculate_fare('car')
print(type(new_calculate))