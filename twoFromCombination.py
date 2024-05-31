import itertools as it
from newGame import *


def twoFromCombination(combination):
    result = []
    for a, b in it.combinations(combination, 2):
        if a < b:
            a, b = b, a
        if (a, b) not in result:
            result.append((a,b))
            yield a, b
            
            
if __name__ == '__main__':
    combination, _ = newGame()
    print(combination)
    for i, (a, b) in enumerate(twoFromCombination(combination)):
        print('%2d  =>  (%3d, %3d)' % (i + 1, a, b))
    print(combination)
        