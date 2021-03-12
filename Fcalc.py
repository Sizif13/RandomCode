import time
import random


def inp(value):
    while True:
        try:
            x = float(input(value))
            return x
        except ValueError:
            lst = ['Input only numbers, please.', 'Sorry, only numbers.', 'Numbers...please.']
            print(random.choice(lst))
            print()


print('F**ked calculator')
print()

while True:
    a = inp('First number: ')
    b = inp('Second number: ')

    while True:
        what = input('What shall I do +, -, *,/ ?: ')
        if what == '+':
            print('Where is my calculator?...')
            time.sleep(2)
            c = a + b
            print('Here you go: ' + str(c))
            break
        elif what == '-':
            print("I'm thinking...")
            time.sleep(2)
            c = a - b
            print('I guess it is: ' + str(c))
            break
        elif what == '*':
            print('One sec...')
            time.sleep(2)
            c = a * b
            print("Don't matter what, we don't know each other: " + str(c))
            break
        elif what == '/':
            print('Hmm...give me a minute...')
            time.sleep(2)
            if b == 0:
                try:
                    c = a / b
                except ZeroDivisionError:
                    print('Division by 0? You seriously? Even I know that is wrong.')
            else:
                c = a / b
                print("I believe it's: " + str(c))
            break
        else:
            print('Hey, you need to choose one of four options.')
            print()

    print()
    ans = input('Continue?\n yep +, nope -: ')
    if ans == '+':
        print()
    elif ans == '-':
        break
    else:
        ans1 = input('OMG, is it so hard to choose? Either + or -. Please: ')
        print()
        if ans1 == '+':
            print()
        elif ans1 == '-':
            break
        else:
            print("For god's sake, f**k it, I'm out!")
            break
