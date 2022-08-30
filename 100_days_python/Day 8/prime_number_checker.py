# It is a coding exercise
# Prime Number Checker
# prime number: a number that can be exctly divided by itself and one

# if number is have a remender as a zero mens it is not prime number
# number = 5
# 5/2 = 
# 5/3 =
# 5/4 =
# if any of the number remender is one then we called as a prime number means the number is not fully divisible.

def prime_checker(number):
    is_prime = True 
    for i in range(2,number):
        if number % i == 0:
            is_prime = False 
    if is_prime:
        print( f"{number} is prime number.") 
    else:
        print(f"{number} is not prime number.")
            
number_input = int(input("Check the number:"))
prime_checker(number=number_input)