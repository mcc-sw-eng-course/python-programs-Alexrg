import random

exit = 0
count = 0
rigth_guess = 0
random_number = random.randint(1,9)

while (exit == 0):
    guess_number = int(input('Enter a number:'))
    if (random_number == guess_number):
        print("You guessed rigth")
        print("The number: {}".format(random_number))
        exit = 1
    else:
        count = count + 1
        print("Wrong guess")
        try_again = input('Type exit if you want to quit:')
        if (try_again == 'exit' or try_again == 'Exit'):
            exit = 1
        else:
            exit = 0

print("Number of tries: {}".format(count))