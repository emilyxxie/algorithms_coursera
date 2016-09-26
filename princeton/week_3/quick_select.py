'''

use the algorithm behind quick sort
in order to quickly find the kth ordered element in an array

'''

import random

def quick_select(n, key):
  low = 0
  high = len(n) - 1
  random.shuffle(n)
  found_key = sort_and_select(n, low, high, key)
  return found_key

def sort_and_select(n, low, high, key):
  if low >= high:
    return
  sorted_pivot = partition(n, low, high)
  if key < sorted_pivot:
    sort_and_select(n, low, sorted_pivot - 1, key)
  elif key > sorted_pivot:
    sort_and_select(n, sorted_pivot + 1, high, key)
  else:
    return sorted_pivot

def partition(n, low, high):
  partition = n[low]
  a = low + 1
  b = high
  while a < b:
    while n[a] < partition:
      a += 1
      if a >= high:
        break
    while n[b] > partition:
      b -= 1
      if b <= low:
        break
    if a > b:
      break
    n[a], n[b] = n[b], n[a]
  if n[b] < n[low]:
    n[b], n[low] = n[low], n[b]
  return b

n = [1, 3, 2, 0, 5, 4]

print(quick_select(n, 4))