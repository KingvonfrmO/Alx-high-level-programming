def print_last_digit(number):
    if number < 0:
        number = -number
        
    last_digit = number % 10
    print("{}".format(last_digit), end="")
    
    return last_digit

print_last_digit(98)
print_last_digit(0)
r = print_last_digit(-1024)
print(r)
