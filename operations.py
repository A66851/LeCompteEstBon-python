def operations(a, b):
    yield a + b, '+'
    if a > b: 
        yield a - b, '-'
    if b > 1:
        yield a * b, 'x'
        if a % b == 0:
            yield a // b, '/'
            
            
if __name__ == '__main__':
    for a, b in [(25, 5), (5, 5), (13, 9), (17, 1)]:
        print('%2d, %2d  =>  %s ' % (a, b, list(operations(a, b))))