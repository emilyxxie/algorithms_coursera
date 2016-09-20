def selection_sort(array):
  for i in range(0, len(array)):
    min_i = i
    for j in range(i, len(array)):
      if array[j] < array[min_i]:
        min_i = j
    array[i], array[min_i] = array[min_i], array[i]
  return array

array = [34, 20, 59, 2, 3, 5, 0]
print(selection_sort(array))