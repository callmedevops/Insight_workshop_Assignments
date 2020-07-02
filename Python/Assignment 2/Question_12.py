# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.


def is_palindrome(str):
    rev_str = str[::-1]
    if str == rev_str:
        return f'{str} is palindrome'
    return f'{str} is not palindrome'


input_string = input("Enter any String ")
print(is_palindrome(input_string))
