from memory_profiler import profile


@profile
def foo():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    # add dome lines here and push it to your branch
    del b
    return a


def get_free_mem_size():
    return 8

def get_total_hd_size():
    return '30GB'

if __name__ == '__main__':
    foo()
