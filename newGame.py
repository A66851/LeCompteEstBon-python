import random


def newGame():
    pans = list(range(1, 11))*2 + list(range(25, 101, 25))
    combination = random.sample(pans, 6)
    target = random.randint(101, 999)
    return combination, target


if __name__ == '__main__':
    combination, target = newGame()
    print(combination, target)
