import math
import sys
'''The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and “W”
    . Write a function turn_clockwise that
     takes one of these four compass points as its parameter, and returns 
     the next compass point in the clockwise direction. Here are some tests that should pass: '''
def turn_clockwise(n):
    if n == "N":
        return "E"
    if n == "E":
        return "S"
    if n == "S":
        return "W"
    if n == "W":
        return "N"
    else:
        return None
# Write the inverse function day_num which is given a day name, and returns its number:
L = {0: "Sunday",1: " Monday",2: "Tuesday", 3: "Wednesday",
4: "Thursday",5: "Friday",6:"Saturday" }
def day_num(i):
    if i in range(6):
        return L[i]
    else:
        return None
# Write a function day_name that converts an integer number 0 to 6 into the name of a day.
def day_name(i):   
    if i == "Sunday":
        return 0
    if i == "Monday":
        return 1
    if i == "Tuesday":
        return 2
    if i == "Wednesday":
        return 3
    if i == "Thursday":
        return 4
    if i == "Friday":
        return 5
    if i == "Saturday":
        return 6
    else:
        return None
def absolute_value(n):   # Buggy version
    """ Compute the absolute value of n """
    if n < 0:
        return 1
    elif n > 0:
        return n
# Write a function that helps answer questions like ‘“Today is Wednesday.
def calc(n,e):
    initial = day_name(n) + e
    return L[initial % 7]
print(calc("Monday",4)) # Testing
print(calc("Sunday",-3))

# Write a function days_in_month which takes the name of a month, and returns the number of days in the month.
def days_in_month(n):
    if n == "January":
        return 31
    if n == "February":
        return 28
    if n == "March":
        return 31
    if n == "April":
        return 30
    if n == "May":
        return 
    if n == "June":
        return 30
    if n == "July":
        return 31
    if n == "August":
        return 31
    if n == "September":
        return 30
    if n == "October":
        return 31
    if n == "November":
        return 30
    if n == "December":
        return 31
# Write a function to_secs that converts hours, minutes and seconds to a total number of seconds
def to_secs(h,m,s):
    return(h*3600) + (m*60)+s

def hours_in(s):
    return math.floor(s / 3600)

def minutes_in(s):
    return (s//60) - ((s // 3600)*60)

def seconds_in(s):
    return math.ceil(((s / 60) - (s // 60)) * 60)

def slope(x1,y1,x2,y2):
    return (y2 - y1) / (x2 - x1)
'''Write a function slope(x1, y1, x2, y2) that returns the slope of the line through the points (x1, y1) and (x2, y2). 
Be sure your implementation of slope can pass the following tests:'''
def intercept(x1,y1,x2,y2):
  y = (slope(x1,y1,x2,y2)*x1) 
  b = y1 - y
  return b

# Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if a < b
def compare(a,b):
    if a > b:
        return 1
    if a < b:
        return -1
    else:
        return 0
'''Write a function called hypotenuse that returns the length of the 
hypotenuse of a right triangle given the lengths of the two legs as parameters:'''
def hypotenuse(leg1,leg2):  
    return math.sqrt(leg1**2+leg2**2) 

'''Write a function called is_even(n) that takes an integer as an argument and returns True
 if the argument is an even number and False if it is odd.'''
def is_even(n):
    return n % 2 == 0

'''Now write the function is_odd(n) 
that returns True when n is odd and False otherwise. Include unit tests for this function too.'''
def is_odd(n):
    return n % 2 != 0

def test(did_pass):

    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(absolute_value(17) == 17)
    test(absolute_value(-17) == 17)
    test(absolute_value(0) == 0)
    test(absolute_value(3.14) == 3.14)
    test(absolute_value(-3.14) == 3.14)
    test(turn_clockwise("N"))
    test(turn_clockwise(3))
    test(day_num(3))
    test(day_num(7))
    test(day_name("Saturday"))
    test(day_name("hello"))
    test(calc("Monday",100))
    test(calc("Tuesday",0))
    test(days_in_month("February"))
    print(to_secs(2,30,2))
    print(hours_in(9010))
    print(minutes_in(9010))
    print(seconds_in(9010))
    print(compare(5,4))
    print(hypotenuse(3,4))
    print(slope(2,4,1,2))
    print(intercept(6,1,1,6))

test_suite()        # Here is the call to run the tests
