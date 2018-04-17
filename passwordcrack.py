from itertools import product
from string import printable
import getpass

password = ()

## function that checks to make sure password meets given length conditions.
def checksize(password):
    if len(password) < 1:
       return False
    elif len(password) > 10:
        return False
    else:
        return True

## while loop runs until user inputed password conditions are met.
while checksize(password) == False:
    password = (getpass.getpass('enter your password up to ten characters! '))
else:
    print(input('press enter and the program will crack the password you entered!'))
    def passwordgenerator():
        count = 0
        while count < 10:
            count += 1
            keywords = (''.join(i) for i in product(printable, repeat = count))
            for combo in keywords:
                yield(combo)

    for testpass in passwordgenerator():

## uncomment to print but it's faster without
##        print(testcombo)

        if testpass == password:
            print('Your password is "{}"! It is not very secure...'.format(testpass))
            input('press enter to close!')
            break

## it could take a while!

