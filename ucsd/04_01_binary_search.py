def binary_search_recursive(nums, key):
  high = len(nums) - 1
  low = 0
  return binary_search_helper(nums, key, high, low)

def binary_search_helper(nums, key, high, low):
  if low >= high:
    return "Item not found"
  mid = (low + high) // 2
  if key == nums[mid]:
    return mid
  if key > nums[mid]:
    low = mid + 1
  else:
    high = mid - 1
  return binary_search_helper(nums, key, high, low)

array = [9, 50]
key = 9
print(binary_search_recursive(array, key))