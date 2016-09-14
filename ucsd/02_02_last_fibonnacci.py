# python3

# finds the last digit of a large fibonnaci number
def last_fibonnaci(n):
  if n == 0:
    return 0
  previous = 0
  current = 1
  for i in range(2, n + 1):

    old_previous = previous
    previous = current
    current += (old_previous % 10)
  return current % 10

n = int(input())
print(last_fibonnaci(n))