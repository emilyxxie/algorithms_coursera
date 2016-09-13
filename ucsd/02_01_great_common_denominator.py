# slower solution

def greatest_common_denominator(x, y):
  gcd = 1

  smaller_number = x if x < y else y
  for i in range(1, smaller_number + 1):
    if x % i == 0 and y % i == 0:
      gcd = i

  return gcd

print greatest_common_denominator(10, 20)

# faster solution TODO