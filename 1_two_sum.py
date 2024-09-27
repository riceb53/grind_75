def twoSum(nums, target):
    desired_number = {}
    for index, value in enumerate(nums):
        correct_value = target - value
        if correct_value in desired_number:
            return [desired_number[correct_value], index]
        else:
            desired_number[value] = index


print(twoSum([2,7,11,15], 9))
        