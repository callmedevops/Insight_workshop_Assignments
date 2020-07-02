# Write a function, is_prime, that takes an integer and returns True if
# the number is prime and False if the number is not prime.


def is_prime(num):
    if num % 2 == 0:
        return False
    elif num == 3 or num == 2:
        return True
    else:
        i = 3
        while i < num:
            if num % i == 0:
                return False
            else:
                return True


input_num = int(input("Enter any Number "))
print(is_prime(input_num))
