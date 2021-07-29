"""
Homework Assignment #5: Basic Loops
*Done: Write a program that prints the numbers from 1 to 100.
*Done: But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
*Done: For numbers which are multiples of both three and five print "FizzBuzz".
    The one hint you'll likely need is: 
    There is a Python operator called "modulo", represented by the percentage sign (%) that gives you the remainder left over after division. So for example:
    6 % 3
    Equals zero. Because after dividing 6 by 3, there is zero leftover. Whereas:
    6 % 4
    Equals 2. Because after dividing 6 by 4, there are 2 left over from the six.
    If that was confusing, don't worry. It will make more sense as you use it. 
    The point is: the modulo operator is useful for finding out if X is a multiple of Y. 
    If it is, then X % Y will yield zero. Knowing this should help you complete this assignment without any issue.
Extra Credit:
*Done: Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime". 
You should print this whenever you encounter a number that is prime (divisible only by itself and one). 
As you implement this, don't worry about the efficiency of the algorithm you use to check for primes. It's okay for it to be slow.
"""
DivisibleByCount =0

for i in range(1,101):
    varResult = ""
    if i%3 == 0:
        varResult += "Fizz"
    if i%5 == 0:
        varResult += "Buzz"

    #Check if is prime number.
    for i2 in range(1,i+1):
        if i%i2 == 0:
            DivisibleByCount += 1
    if DivisibleByCount == 2:
        varResult +="Prime"
    DivisibleByCount =0
    
    if varResult == "":
        varResult = i

    print(varResult)
    varResult = ""