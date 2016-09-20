# python3
# polynomial multiplication, big O(n**2) solution

def polynomial_multiplication(p1, p2, n):
  result = [0] * (n * 2 - 1)
  for i, num in enumerate(p1):
    for j, num2 in enumerate(p2):
      result[i + j] += num * num2
  return result

p1 = [3, 2, 5]
p2 = [5, 1, 2]
print(polynomial_multiplication(p1, p2, 3))