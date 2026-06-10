import random


def main():
    show_header()

    the_number = random.randint(1, 100)

    count = 0
    while True:
        guess = get_guess()
        if not guess:
            continue

        count += 1
        if evaluate_guess(guess, the_number):
            break

    print(f"You go the nubmer in {count} attempts. Thanks for playing, bye")


def evaluate_guess(guess, number):
    if guess == number:
        print(f"Correct! I was thinking of {number}")
    if guess < number:
        print("That's too LOW")
    if guess > number:
        print("That's too HIGH")

    return guess == number


def get_guess():
    try:
        text = input("What number am I thinking of?")
        val = int(text)
        if val < 1 or val > 100:
            print("Please enter a number between 1 and 100")
            return None
        return val
    except:
        print(f"{val} is not an integer between 1 and 100")
        return None


def show_header():
    print("-------------------------------------------");
    print("|                                         |");
    print("|           Python HIGH / LOW GAME        |");
    print("|                                         |");
    print("-------------------------------------------");
    print();
    print("I'm thinking of a number between 1 & 100.");
    print("How many steps can you guess it in?");
    print();


if __name__ == '__main__':
    main()