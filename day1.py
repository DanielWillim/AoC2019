def fuel_cost(mass):
    mass_fuel = (mass // 3) - 2
    
    if mass_fuel <= 0:
        return 0
    
    return mass_fuel + fuel_cost(mass_fuel)

inp = open('inp_day1', "r")

lines = inp.readlines()

total_cost = 0

print(fuel_cost(14))
print(fuel_cost(100756))

for line in lines:
    total_cost += fuel_cost(int(line))

print(total_cost)
inp.close()
