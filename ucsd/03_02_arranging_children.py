import sys
# python3

# arrange children in the smallest number of groups such that in every group
# each child is at most 1 year apart in age

# naive implementation
def arranging_children(children):
  child_count = len(children) - 1
  children.sort()
  # base child is the youngest child in any given group
  base_child = 0
  groups = 0
  while base_child < child_count:
    in_group = 0
    next_child = base_child + 1
    while children[next_child] - children[base_child] <= 1 and next_child < child_count:
      in_group += 1
      next_child += 1
    # once we've broken out of the loop
    # all children counted in the group are taken out of consideration
    # and base child becomes the next unaccounted child
    base_child += in_group + 1
    groups += 1

  return groups

children_ages = [3.16, 3.6, 4.5, 5]
print(arranging_children(children_ages))

