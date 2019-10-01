from random import randint


def guess_number():
    return randint(1, 100)


welcome = """
Hi gamer. Lets play the game.
Guess the number I picked between 1 and 100.
Will se how rounds it will take
 """


def get_answer():

    while True:

        answer = input('Enter a number (1-100): ')

        try:
            number = int(answer)

            if number > 100 or number < 1:
                print('Number is out of range. Lets try again')
                continue

        except ValueError:
            print('Are u sure you entered not a string? Lets try again. ')
            continue

        return number


def random_number_game():

    print(welcome)
    guessed_number = guess_number()
    answer = get_answer()
    counter = 1

    while answer != guessed_number:

        if answer > guessed_number:
            print('You are taking to hi!. Try again.')
            answer = get_answer()

        if answer < guessed_number:
            print('Sorry, pal. Too low. Try again')
            answer = get_answer()

        counter += 1

    print('Horrey, you"ve managed to guess the number in {} tries'.format(counter))


if __name__ == '__main__':
    random_number_game()