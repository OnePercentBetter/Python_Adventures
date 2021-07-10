 # Result of the following:
"Python"[1] # y
"Strings are sequences of characters."[5] # g
len("wonderful") # 8
print("Mystery"[:4]) # Myst
print("p" in "Pineapple") #True
"apple" in "Pineapple" # True
"pear" not in "Pineapple" # True
print("apple" > "pineapple") #False
print("pineapple" < "Peach") # False because
    #Caps take priority in comparison to case-sensitve

def find(strng, ch):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1


#Modify:
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    print(letter + suffix)

def count_letters(n,a):
    count = 0
    for char in n:
        if char == a:
            count += 1
    return count
print(count_letters("Hello","l"))

def count_letters(n,a,extra=0):
    ix = extra
    while ix < len(n):
        if n[ix] == a:
            return ix
        ix += 1
    return -1
#Print a multiplication table
print(count_letters("Hello","l"))
def multiplication():
    for i in range(1,13):
        print(i,"\t",end=" ")
    print("\n")
    for i in range(1,13):
        for j in range(1,13):
            print(i*j,"\t",end=" ")
        print("\n")
print(multiplication())
# Write a function that reverses its string argument
def reverse(n):
    empty = ""
    reversal = -1
    negative_absolute = -(len(n))
    for i in n:
        if reversal >= negative_absolute:
            empty += n[reversal]
        reversal -= 1
    return empty
print(reverse("Hello"))


#Write a function that mirrors its argument
def mirror(n):
    return n + reverse(n)
print(mirror("hell0"))



# Write a function that removes all occurrences of a given letter from a string:
def removal(word,character):
    empty = ""
    for x in word:
        if character not in x:
            empty += x
    return empty

print(removal("Hello","o"))
    # Write a function that recognizes palindromes
def palindrome(n):
    return n == reverse(n)
print(palindrome("Hello"))

# Write a function that counts how many times a substring occurs in a string
def occurrs(n,phrase):
    return n.count(phrase)

print(occurrs("hellololo","lo"))

def remove_string(n,phrase):
    empty = ""
    for x in n:
        if phrase not in x:
            empty += x
    return empty
print(remove_string("hello","l"))







'''triple = "'hi my name is __'"
def remove_punctuation(n):
    empty_string = ""
    count = 0
    for letter in n:
        if letter != "'":
            empty_string += letter
            if letter == "e":
                count += 1
    return print("Your text contains+ str(len(empty_string.split())) + " words, of which " + count + " (" + ((str(len(empty_string.split())) /((str(len(empty_string.split()) - str((count)-1))) + "%) contains an 'e'"))))
remove_punctuation(triple)'''


'''for i in range(1, 12):
    print(1, "\t", 2*i, "\t", 3*i, "\t", 4*i, "\t",
        5*i, "\t", 6*i, "\t", 7*i, "\t", 8*i, "\t", 9*i, "\t", 10*i, "\t", 11*i,
        "\t", 12*i)'''









'''   #Remove all Vowels in a given string
def remove_vowels(s):
    vowels = "aeiouAEIOU"
    s_sans_vowels = ""
    for x in s:
        if x not in vowels:
            s_sans_vowels += x
    return s_sans_vowels
print(remove_vowels("compsci") == "cmpsc")
print(remove_vowels("aAbEefIijOopUus") == "bfjps")'''

'''def find(strng, ch):
    """
      Find and return the index of ch in strng.
      Return -1 if ch does not occur in strng.
    """
    ix = 0
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

test(find("Compsci", "p") == 3)
test(find("Compsci", "C") == 0)
test(find("Compsci", "i") == 6)
test(find("Compsci", "x") == -1)'''
