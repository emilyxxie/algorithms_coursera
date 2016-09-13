def factorial(n):
  total = 1
  for i in range(1, n + 1):
    total *= i
  return total

print factorial(0)



def factorial_recursive(n):
  if n <= 1:
    return 1
  return n * factorial_recursive(n - 1)


print factorial_recursive(6)