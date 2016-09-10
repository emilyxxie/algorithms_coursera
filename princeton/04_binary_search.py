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
    # and idea here
    left = mid_index + 1
    return binary_search(array, left, right, key)


# test case
array = [6, 13, 14, 25, 33, 43, 51, 53, 64, 72, 84, 93, 95, 96, 97];
print binary_search(array, 0, len(array) - 1, 43);

# TODO:
def binary_search_non_recursive(array, key):
  pass