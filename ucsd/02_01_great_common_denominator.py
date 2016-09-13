# slower solution, slightly optimized

def greatest_common_denominator(x, y):
  gcd = 1

  smaller_number = x if x < y else y
  for i in range(1, smaller_number + 1):
    if x % i == 0 and y % i == 0:
      gcd = i

  return gcd

# print in python 3 requires parenthesis
print(greatest_common_denominator(10, 20))

# faster solution using Euclidean Algorithm
# Concept is that when you subtract the smaller number from the larger number
# then the smaller number and the subtracted number will yield the same GCD
# keep doing this until x == y. This means that you have reached your GCD

def gcd_euclidean(x, y):
  if x == y:
    return x
  smaller = x if x < y else y
  larger = y if y > x else x
  diff = larger - smaller
  return gcd_euclidean(diff, smaller)

print(gcd_euclidean(357, 234))