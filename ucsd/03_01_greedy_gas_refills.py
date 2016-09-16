# python3
# get the minimum number of refills for a given route

def min_refills(gas_stations, gas_capacity):
  current = 0
  refills = 0
  i = 1
  while current + i < len(stations) - 1:
    if current + i ==
    if gas_stations[current + i] - gas_stations[current] <= gas_capacity:
      # try the next station over as we want to go as far as we can without refilling
      i += 1
    else:
      current += (i - 1)
      i = 1
      refills += 1
  return refills

# print(min_refills(stations, 400))



# refactored version, closer to what was shown in lecture
# looks essentially the same, except we account for impossible scenarios
def min_refills(stations, n, capacity):
  current = 0
  refills = 0
  while current < n:
    print("current: %d" % (current))
    last_refill = current
    while current < n and \
    stations[current + 1] - stations[last_refill] <= capacity:
      current += 1
    # if this line is true, this means the above while statement never executed
    if current == last_refill:
      return "Sorry, the trip is impossible to do."
    if current < n:
      refills += 1

  return refills



stations = [0, 200, 375, 550, 750, 950]
print(min_refills(stations, len(stations) - 1, 400))
