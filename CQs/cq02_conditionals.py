"""Junyi (Johnny) Zhong's condition's practice"""

__author__ = "730776350"


def guess_a_number() -> None:
    """declare local variables here"""
    secret: int = 7
    guess: int = int(input("Guess a number:"))
    print("Your guess was", guess)
    """use conditions to determine whether if the guess is equal to the secret number"""
    if guess == secret:
        print("You got it!")
    elif guess < secret:
        print("Your guess was too low! The secret number is", secret)
    elif guess > secret:
        print("Your guess was too high! The secret number is", secret)

    return None


if __name__ == "__main__":
    guess_a_number()
