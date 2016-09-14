# python3

# ugly brute force implementation
def least_common_multiple(a, b):
  if a == b:
    return b
  x = a if a < b else b  # by default, let's make the smaller number x
  y = a if a > b else b  # and the larger one y
  y_multiples = []
  x_current = x
  y_current = y
  i = 1
  while x_current not in y_multiples:
    y_current = y * i
    y_multiples.append(y_current)
    x_current = x * i
    i += 1
  return x_current


'''
better implementation.
this employs the property that for any two given pairs of numbers,
the greatest common divisor and the least common multiple will create a product that is equal the product of the initial pair
'''

def gcd_euclidean(x, y):
  if x == y:
    return x
  smaller = x if x < y else y
  larger = y if y > x else x
  diff = larger - smaller
  return gcd_euclidean(diff, smaller)


def lcm_refactored(x, y):
  return (x * y) // gcd_euclidean(x, y)

x = int(input())
y = int(input())
print(lcm_refactored(x, y))
