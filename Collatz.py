def collatz(number):
    if (number % 2 == 0):
        next = int(number / 2)
        print (next)
        return next
    else:
        next = number * 3 + 1
        print (next)
        return next

print('Type in a number. We\'ll run the Collatz sequence on it.')
try: 
    number = int(input())
    while (number != 1):
        number = collatz(number)
except ValueError:
    print("Please enter an integer.")

