from newGame import * # type: ignore
from solver import * # type: ignore
import time

combination, target = newGame()
print(combination, target )

startTime = time.time()
status, nearestResult, nearestToTarget = solver(target, combination)
finalTime = time.time()
elapsedTime = finalTime - startTime

if status == True:
    print('\nThe first solution found :\n')
else:
    print('\nNearest Solution to target : %d \n' % (nearestToTarget))

print(nearestResult)
print('CPUtime = %5.1f ms.\n' % (1000*elapsedTime))


