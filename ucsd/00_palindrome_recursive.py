def is_palindrome(string):
  start = 0
  end = len(string) - 1
  return detect_palindrome(string, start, end)

# initial solution
def detect_palindrome(string, start, end):
  if start >= end:
    return True
  start += 1
  end -= 1
  if string[start] != string[end]:
    return False
  return detect_palindrome(string, start, end)


# refactored solution
def detect_palindrome_refactored(string):
  if len(string) < 2:
    return True
  # use negative 1 to get the last item in an array
  if string[0] != string[-1]:
    return False
  return detect_palindrome_refactored(string[1:-1])

string = "anna"
print detect_palindrome_refactored(string)