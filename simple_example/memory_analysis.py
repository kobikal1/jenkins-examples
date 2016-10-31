from memory_profiler import profile


@profile
def foo():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    # add dome lines here and push it to your branch
    c = 3 + b
    del b
    return a

if __name__ == '__main__':
    foo()
