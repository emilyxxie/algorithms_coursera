# python3
# fractional knapsack brute force / initial solution

def fractional_knapsack(items, capacity):
  knapsack = []
  total = 0
  items.sort(key = lambda x: (x[1] / x[2]) , reverse = True)
  for i, item in enumerate(items):
    knapsack.append([item[0], 0])
    while total < capacity and item[2] > 0:
      knapsack[i][1] += 1
      item[2] -= 1
      total += 1
  else:
    return knapsack

items = [["bread", 18, 3], ["cheese", 14, 2], ["trail_mix", 20, 4]]
print(fractional_knapsack(items, 7))