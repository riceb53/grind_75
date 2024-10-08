import pdb

def firstBadVersion(n):
    middle = n // 2
    left = 0
    right = n
    while right - left > 1:
        pdb.set_trace()
        if isBadVersion(middle):            
            right = middle
        else:
            left = middle
        middle = (right + left) // 2
    return right
        

def isBadVersion(number):
    if number >= 4:
        return True
    else:
        return False


print(firstBadVersion(5) == 4)

#  n = 5, bad = 4
# n = 1, bad = 1