import random

# quick sort - goes through and sorts the pivots in place
def quick_sort(n):
  low = 0
  high = len(n) - 1
  random.shuffle(n)
  sort(n, low, high)
  return n

def sort(n, low, high):
  if low >= high:
    return
  sorted_pivot = partition(n, low, high)
  sort(n, low, sorted_pivot - 1)
  sort(n, sorted_pivot + 1, high)

# pick partition point. traverse the array using two pointers, a + b
# and swap array[a] and array[b] if they are on the wrong side of partition
# until the two indexes cross
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

n = random.sample(range(0, 100), 100)
print(quick_sort(n))