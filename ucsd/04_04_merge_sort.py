import random
from copy import copy

def merge_sort(nums):
  if len(nums) <= 1:
    return nums
  mid = len(nums) // 2
  left = merge_sort(nums[:mid])
  right = merge_sort(nums[mid:])
  return sort(left, right)

def sort(left, right):
  result = []
  while len(left) > 0 and len(right) > 0:
    if left[0] <= right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  remaining = left if len(left) > len(right) else right
  return result + remaining

number_list = random.sample(
  range(0, 1000),
  1000
)
# print(merge_sort(number_list))
number_list = merge_sort(number_list)
listb = copy(number_list)
listb.sort()
assert merge_sort(number_list) == listb