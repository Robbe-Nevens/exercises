# Write your code here
def digit_sum(int):
    sum = 0
    while int > 0:
        sum += last_digit(int)
        int = remove_last_digit(int)
    return sum

def last_digit(int):
    return int%10

def remove_last_digit(int):
    return int//10