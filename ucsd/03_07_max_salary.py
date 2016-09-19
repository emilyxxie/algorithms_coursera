# python3

'''
Find the max salary for any given set of integers
TODO: Must account for integers above 9
'''

def find_max_salary(nums):
  answer = []
  for i in range(0, len(nums)):
    largest = max(nums)
    answer.append(largest)
    nums.remove(largest)
  return "".join(str(x) for x in answer)

nums = [23, 39, 92]
print(find_max_salary(nums))