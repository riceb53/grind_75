import pdb
def canConstruct(ransomNote, magazine):
    magazine_chars =  {}
    for char in magazine:
        if char in magazine_chars:
            magazine_chars[char] += 1
        else:
            magazine_chars[char] = 1        

    for char in ransomNote:
        if char in magazine_chars:
            magazine_chars[char] -= 1        
            if magazine_chars[char] < 0:
                return False
        else:
            return False
    return True
    # for each element in ransomNote make sure magazine has at least as many chars of that
    # loop through magazine and remove chars based on current char, 


print(canConstruct("a", "b") == False)
print(canConstruct("aa", "ab") == False)
print(canConstruct("aa", "aab") == True)




