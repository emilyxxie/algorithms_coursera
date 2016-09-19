# python3

# find the minimum number of coins needed to change input value
# into coins with denominations 1, 5, 10

def min_coins(n):
  coins = [10, 5, 1]
  min_coins = 0
  i = 0
  while n > 0:
    if n - coins[i] < 0:
      i += 1
      continue
    n -= coins[i]
    min_coins += 1
  return min_coins

n = int(input())
print(min_coins(n))
