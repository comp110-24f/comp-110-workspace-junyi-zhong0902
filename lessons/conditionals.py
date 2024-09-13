"""Practicing my conditionals"""


def less_than_10(num: int) -> None:
    """Tell us if num < 10"""
    dub: int = num * 2  # 14
    dub = dub - 1  # 13
    print(dub)
    if num < 10:
        print("small numer!")
    else:
        print("Big number!")
    print("this is the end of the function!")


print(less_than_10(num=7))


def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    else:
        return "not match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
