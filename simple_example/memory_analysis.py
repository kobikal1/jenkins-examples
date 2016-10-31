from memory_profiler import profile


@profile
def foo():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    # add dome lines here and push it to your branch
    # this is my change
    # this is my change 2
    del b
    return a

if __name__ == '__main__':
    foo()
