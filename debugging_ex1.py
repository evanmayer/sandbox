# Run a working code to get familiar with running a debugger.

def fib(N):
    '''
    Return the Nth Fibonacci number. Note: this function is not optimized.

    Parameters
    ----------
    N : int
        Which Fibonacci number to return; 0th Fibonacci number is 0, 1st is 1.

    Returns
    -------
    int
        Nth Fibonacci number
    '''
    if N == 0:
        return N
    if N == 1:
        return N
    else:
        prev1 = fib(N - 1)
        prev2 = fib(N - 2)
        return prev1 + prev2

if __name__ == '__main__':
    print(fib(10))