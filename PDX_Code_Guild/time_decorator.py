import time

def time_check(function, *args):
    def wrapper_func(args):
        t0 = time.time()
        count = function(args)
        t1 = time.time()
        return count, t1 - t0
    return wrapper_func

@time_check
def get_array(array):
    count = 0
    for i in array:
        count += 1
    return count

print(get_array([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))

