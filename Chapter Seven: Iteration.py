# Chapter Seven
    #Write a function to count how many odd numbers are in a list.
def sum_odd(n):
    count = 0
    for i in n:
        if i % 2 != 0:
            count += i
    return count
print(sum_odd([1,2,3,4,5]))

    #Sum up all the even numbers in a list
def sum_even(n):
    count = 0
    for i in n:
        if i % 2 == 0:
            count += i
    return count
print(sum_even([1,2,3,4,5]))

    #Sum up all the negative numbers in a list.
def sum_negative(n):
    count = 0
    for i in n:
        if i <= 0:
            count += i
    return count
print(sum_even([-1,-2,-3,4,5]))

    #Count how many words in a list have length 5.
def leng_five(n):
    count = 0
    for i in n:
        if len(i) == 5:
            count += 1
    return count 
lis = ("Hello","Why","You","Mourn")
print(leng_five(lis))

    #Sum all the elements in a list up to but not including the first even number. 
    #(Write your unit tests. What if there is no even number?)
def sum_elements(n):
    count = 0
    for i in n:
        if i % 2 == 0:
            break
        count += i
    return count
ev = [2,3,4,5,6]
print(sum_elements(ev))

    #Count how many words occur in a list up to and including the first
    #occurrence of the word “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)
def sam(n):
    occurrences = 0
    for i in n:
        if i == "sam":
            break
        occurrences += 1
    return occurrences 
sam3 = ("why","where","when","sam")
print(sam(sam3))

def sqrt(n):
    approx = n/2.0     # Start with some or other guess at the answer
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better

    # Test cases
print(sqrt(25.0))
print(sqrt(49.0))
print(sqrt(81.0))

    #Write a function print_triangular_numbers(n) that prints out the first n triangular 
    #numbers. A call to print_triangular_numbers(5) would produce the following output:
def print_triangular_number(n):
    count = 0
    for i in range(1,n+1):
        count += i
        print(i,"\t",count)
print_triangular_number(5)

    #Write a function, is_prime, which takes a single integer argument and returns True when the argument 
    #is a prime number and False otherwise. Add tests for cases like this:
def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
        else:
            return True
print(is_prime(32))

    #What will num_digits(0) return? 
    #Modify it to return 1 for this case. 
    #Why does a call to num_digits(-24) result in an infinite loop?
def num_digits(n):
    count = 0
    if n == 0:
        return 1
    else:
        while n != 0:
            count = count + 1
            n = abs(n) // 10
            print(n)
    return count
print(num_digits(-24))
    #Write a function num_even_digits(n) 
    #that counts the number of even digits in n. These tests should pass:
def num_even_digits(n):
    count = 0
    while n != 0:
        if n % 2 == 0:
            count += 1
        n = n // 10
    return count
print(num_even_digits(123456))

    #Write a function sum_of_squares(xs) 
    #that computes the sum of the squares of the numbers in the list xs
def sum_of_squares(n):
    count = 0
    for i in n:
        count += i*i
    return count
er = [2,3,4]
print(sum_of_squares(er))

# Your friend will complete this function
def play_once(human_plays_first):
    """
       Must play one round of the game. If the parameter
       is True, the human gets to play first, else the
       computer gets to play first.  When the round ends,
       the return value of the function is one of
       -1 (human wins),  0 (game drawn),   1 (computer wins).
    """
    # This is all dummy scaffolding code right at the moment...
    import random                  # See Modules chapter ...
    rng = random.Random()
    # Pick a random result between -1 and 1.
    result = rng.randrange(-1,2)
    print("Human plays first={0},  winner={1} "
                       .format(human_plays_first, result))
    return result
