import pdb
def isPalindrome(s):
    l = 0
    r = len(s) - 1
    while l < r:
        # print(s[l], s[r])
        # pdb.set_trace()
        if not s[l].isalnum():
            l += 1
        elif not s[r].isalnum():
            r -= 1
        else:
            if s[l].lower() == s[r].lower():
                l += 1
                r -=1
            else:
                return False
    return True

print(isPalindrome("A man, a plan, a canal: Panama") == True)
print(isPalindrome("race a car") == False)
print(isPalindrome(" ") == True)
    # two pointer
    # loop while l < r
    # if char is nonalphanumeric increment
    # downcase it
    # verify that val of l and r are the same
    
        