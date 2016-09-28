def binary_search(array, left, right, key):
  if len(array) == 0:
    return False

  mid_index = (left + right) // 2

  if array[mid_index] == key:
    return mid_index

  if array[mid_index] > key:
    # subtract one from midpoint since we've already evaluated the element that index
    right = mid_index - 1
    return binary_search(array, left, right, key)
  else:
    # and add index here
    left = mid_index + 1
    return binary_search(array, left, right, key)


# test case
array = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97];
print binary_search(array, 0, len(array) - 1, 43);



def binary_search_non_recursive(array, key):
  total = 0
  if len(array) == 0:
    return

  start = 0
  end = len(array)

  while (start != end):
    midpoint = (start + end) // 2
    if key == array[midpoint]:
      return midpoint
    elif key <= array[midpoint]:
      end = midpoint
    else:
      start = midpoint
  else:
    return "not found"

print binary_search_non_recursive(array, 97);
