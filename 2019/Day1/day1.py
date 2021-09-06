filename = "Day1/input.txt"
file = open(filename, "r")
def fuel_required(mass):
   additional_required = int(mass/3)-2
   if(additional_required <= 0):
      return 0
   else:
      return additional_required + fuel_required(additional_required)

total_fuel=0
print(fuel_required(14))
print(fuel_required(1969))
print(fuel_required(100756))

for line in file:
   total_fuel += fuel_required(int(line))
   print(total_fuel)

# tests
if(fuel_required(14) == 2 and print(fuel_required(1969))==966 and fuel_required(100756) == 50346):
   print("OK")