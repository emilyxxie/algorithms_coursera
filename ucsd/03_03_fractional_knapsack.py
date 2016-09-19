# python3
# fractional knapsack brute force / initial solution

def fractional_knapsack(items, capacity):
  knapsack = []
  items.sort(key = lambda x: (x[1] / x[2]) , reverse = True)
  for i, item in enumerate(items):
    if capacity == 0:
      return knapsack
    knapsack.append([item[0], 0])
    while capacity > 0 and item[2] > 0:
      knapsack[i][1] += 1
      item[2] -= 1
      capacity -= 1
  return knapsack

items = [["bread", 18, 3], ["cheese", 14, 2], ["trail_mix", 20, 4]]
print(fractional_knapsack(items, 7))