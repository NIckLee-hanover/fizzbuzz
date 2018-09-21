"""
fizzbuzz.py
Author: Nick Lee
Credit: <list sources used, if any>

Assignment:FizzBuzz

Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.

We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:

How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
"""
amount = int(input("How many numbers shall we print? "))
fizz = int(input("For multiples of what number shall we print 'Fizz'? "))
buzz = int(input("For multiples of what number shall we print 'Buzz'? "))

for i in range(amount):
    F = str(round((i/fizz),1))
    print(len(F))

"""
for i in range(1,amount):
    F = [i for i in amount]
    print (F)
    for j in range(6):
        
        if F[j] == ".":
            print(i)
            break
        elif j == len(F):
                print("Fizz")
                
        print(F[2])
    B = (i/buzz)
    for j in range(len(B)):
        if B[j] == int(".") :
            print(i)
            break
        elif j == len(B):
                print("Buzz")
    """







