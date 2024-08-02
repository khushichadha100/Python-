#important python practical programs:-
'''
#check if string is palindrome or not
str=input("enter word to check palindrome or not:")
temp=str[::-1]
print(str)
print(temp)
if str==temp:
    print("yes palindrome")
else:
    print("not palindrome")



#finding factorial of a no. via recursion
def fact(x):
    if x==1:
        return 1
    else:
       return x*fact(x-1)

a=int(input("enter no. for factorial:"))
res=fact(a)
print("factorial of ",a,"is:",res)

#Prime no:-
def is_prime_simple(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
     

# Example: Check if 13 is a prime number using the simple method
num_to_check = int(input("enter no."))
if is_prime_simple(num_to_check):
    print(num_to_check,"is prime")
else:
    print(num_to_check,"is not prime")

#Armstrong:-
def is_armstrong_alternative(number):
    temp = number#153
    length = len(str(number))#3
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** length
        temp //= 10

    return total == number

# Example: Check if 153 is an Armstrong number using the alternative method
num_to_check = int(input("enter no"))
print(f"{num_to_check} is {'an Armstrong number' 
      if is_armstrong_alternative(num_to_check) else
      'not an Armstrong number'}.")

'''
#Fibonacci series:-
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Example: Print the first 10 Fibonacci numbers
n = int(input("enter no."))
result = fibonacci(n)
print(result)
 
 