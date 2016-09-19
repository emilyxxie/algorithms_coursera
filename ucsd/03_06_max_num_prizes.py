#python3

def max_num_prizes(n):
  prizes = []
  for i in range(1, n):
    prizes.append(i)
    if n - sum(prizes) < i:
      return prizes, len(prizes)
  return prizes, len(prizes)

n = int(input())
print(max_num_prizes(n))