# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:



def search(nums, target):
    l = 0
    r = len(nums) - 1
    while l <= r:
        center = (l + r) // 2        
        if nums[center] > target:
            r = center - 1
        elif nums[center] < target:
            l = center + 1
        else:
            return center
    return -1
    
    # l and r pointers
    # pick middle
    # compare that to target
    # adjust l or r appropriately
    # keep going until you find target or middle is either l or r
    


print(search([-1,0,3,5,9,12], 9) == 4)
print(search([-1,0,3,5,9,12], 2) == -1)
print(search([5], 5) == 0)
    