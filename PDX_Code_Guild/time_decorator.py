import timeit

def time(function, *args):
    def wrapper_func(args):
        return timeit.timeit(str(function(args))), function(args)
    return wrapper_func

@time
def get_array(array):
    count = 0
    for i in array:
        count += 1
    return count

print(get_array([1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]))

