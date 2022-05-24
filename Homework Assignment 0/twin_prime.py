#Author: Janmejay Mohanty
#Cite: https://www.w3schools.com/python/python_for_loops.asp, https://www.geeksforgeeks.org/twin-prime-numbers/
def check_prime_number(n):                                           # Prime number checking function                            
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def print_twin_prime_numbers(y):                                     # Twin prime function
    for i in range(2, y):
        j = i + 2
        if(check_prime_number(i) and check_prime_number(j)):
            print("(",i ,",", j,")")

x = int(input("Enter a number upto generating twin prime: "))        # User input for where till the User's choice to print Twin prime numbers

print_twin_prime_numbers(x)                                          # Generating the twin prime numbers
