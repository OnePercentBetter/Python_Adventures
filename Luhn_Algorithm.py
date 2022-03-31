import random
def luhn_algo(n):
        strung = ""
        y = str(n)
        fifteen = n // 10
        new = ""
        sum_digit = 0
        while fifteen != 0:
            digit = fifteen % 10
            if digit % 2 == 1:
                strung += str(digit)
            else:
                strung += str(digit)
            fifteen //= 10
        fixed = int(strung[::-1])
        new_num = [int(i) for i in str(fixed)]
        for i in range(len(new_num)):
            if i % 2 == 0:
                if new_num[i]*2 > 9:
                    new += ((str(new_num[i]*2 % 10 + 1)))
                else:
                    new += str(new_num[i]*2)
                if (new_num[i]) > 9:
                    new += str((new_num[i]% 10) + 1)
            else:
                new += str(new_num[i])
            i += 1
        for i in new:
            if i.isdigit() == True:
                q = int(i)
                sum_digit += q
        sum_digit += int(y[15])
        return sum_digit
last_digit = int(random.randint(0,9))
card_number = int("400000" + str(random.randint(100000000,999999999)) + str(last_digit))
def check_sum():
    return (luhn_algo(card_number)) % 10 == 0
while check_sum != True:
        last_digit = int(random.randint(0,9))
        card_number = int("400000" + str(random.randint(100000000,999999999)) + str(last_digit))
        if(check_sum()) == True:
            break

initial = int
second_initial = int
while initial != 0:
    initial = int(input("1. Create an account \n2. Log into account \n0.Exit\n"))
    if initial == 1:
        print("Your account has been created")
        print(card_number)
        pin = random.randint(1000,9999)
        print(pin)
        if initial == 2:
            verify_card = int(input("Enter your card number:\n"))
            verify_pin = int(input("Enter your pin:\n"))
            if verify_card == card_number and pin == verify_pin:
                print("You have successfully logged in!")
                while second_initial != 0:
                    print("1. Balance\n2. Log out\n0. Exit\n")
                    second_initial = int(input())
                    if second_initial == 1:
                        print("Balance: 0")
                    if second_initial == 2:
                        print("You have successfully logged out")
                        break
                else: 
                    print("Bye!")
                    print(exit)
            else:
                print("Wrong card number or PIN!")
    else:
        print("Bye!")
        print(exit) 
