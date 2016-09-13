# calculates the nth fibonnaci number
def fibonnaci(n):
  previous = 0
  current = 1

  # subtract 2 to account for the two starting numbers
  for i in range(0, n - 2):
    old_previous = previous
    previous = current
    current = old_previous + current

  return current

print fibonnaci(6)
