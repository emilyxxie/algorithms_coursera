#python3

def max_num_prizes(n):
  prizes = []
  for i in range(1, n + 1):
    prizes.append(i)
    if n - sum(prizes) < i:
      prizes[-1] += n - sum(prizes)
      print_result(prizes)
      return
  print_result(prizes)

def print_result(array):
  print(len(array))
  print(" ".join(str(x) for x in array))

n = int(input())
max_num_prizes(n)