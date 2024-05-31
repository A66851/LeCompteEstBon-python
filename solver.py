from newGame import *
from twoFromCombination import *
from operations import *


def solver(target, combination):
    def _solver(target, combination, currentResult):#, nearestResult, nearestToTarget):
        global  nearestResult, nearestToTarget
        for a, b in twoFromCombination(combination):
            for result, operation in operations(a, b):
                newResult = currentResult + '%d %s %d = %d\n' % (a, operation, b, result)
                if abs(target - result) < abs(target - nearestToTarget):
                    nearestResult, nearestToTarget = newResult, result
                    #print(nearestResult, nearestToTarget)
                    if result == target:
                        return True
                newCombination = combination + [result]
                newCombination.remove(a)
                newCombination.remove(b)
                if _solver(target, newCombination, newResult):#, nearestResult, nearestToTarget):
                    return True
        return False
    
    
    global  nearestResult, nearestToTarget
    currentResult, nearestResult, nearestToTarget = '', '', 0
    status = _solver(target, combination, currentResult)#, nearestResult, nearestToTarget)
    return status, nearestResult, nearestToTarget


if __name__ == '__main__':
    combination, target = newGame()
    print(combination, target )
    
    status, nearestResult, nearestToTarget = solver(target, combination)
    
    if status == True:
        print('\nSolution found :\n')
    else:
        print('\nNearest Solution to target : %d \n' % (nearestToTarget))
    
    print(nearestResult)
    print(combination, target )
    