"""Write a Python class to find validity of a string of parentheses, '(',
')', '{', '}', '[' and ']. These brackets must be close in the correct order,
for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid"""
globvar = 0


def set_globvar_to_one():
    global globvar
    globvar = 1


def print_globvar():
    print(globvar)


set_globvar_to_one()
print_globvar()
