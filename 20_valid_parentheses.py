def isValid(s):
    parens_dict = {
        "{": "}",
        "(": ")",
        "[": "]"
    }
    opened_parens = []
    for char in s:
        if char in parens_dict:
            opened_parens.append(char)
        else:
            if parens_dict[opened_parens[-1]] == char:
                opened_parens.pop()
            else:
                return False
    if len(opened_parens) > 0:
        return False
    else:
        return True

print(isValid("()") == True)
print(isValid("()[]{}") == True)
print(isValid("(]") == False)
print(isValid("([])") == True)
