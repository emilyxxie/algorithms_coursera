# python 3
# get the minimum number of refills for a given route

def min_refills(gas_stations, gas_capacity):
  current = 0
  refills = 0
  i = 1
  while not current + i > len(stations) - 1:
    if gas_stations[current + i] - gas_stations[current] <= gas_capacity:
      # try the next station over as we want to go as far as we can without refilling
      i += 1
    else:
      current += (i - 1)
      i = 1
      refills += 1
  return refills

stations = [0, 200, 375, 550, 750, 950]

print(min_refills(stations, 400))

