'''
Assume you are given two dictionaries d1 and d2, each with integer keys and
integer values. You are also given a function f, that takes in two integers,
performs an unknown operation on them, and returns a value.

Write a function called dict_interdiff that takes in two dictionaries (d1 and d2).
The function will return a tuple of two dictionaries: a dictionary of the
intersect of d1 and d2 and a dictionary of the difference of d1 and d2,
calculated as follows:

intersect: The keys to the intersect dictionary are keys that are common in
both d1 and d2. To get the values of the intersect dictionary, look at the
common keys in d1 and d2 and apply the function f to these keys' values -- the
value of the common key in d1 is the first parameter to the function and the
value of the common key in d2 is the second parameter to the function. Do not
implement f inside your dict_interdiff code -- assume it is defined outside.

difference: a key-value pair in the difference dictionary is (a) every key-value
pair in d1 whose key appears only in d1 and not in d2 or (b) every key-value pair
in d2 whose key appears only in d2 and not in d1.
'''

def f(a,b):
  '''simple test function that adds a and b'''
  return a + b

def dict_interdiff(d1, d2):

    # INTERSECTION

    # find common keys across d1 and d2
    common_keys = {key for key in d1.keys() if key in d2.keys()}

    #initialize a dict from that set of keys, and 0 values
    intersection_dict = dict.fromkeys(common_keys, 0)

    # grab the values associated with common keys from d1 and d2, for use in f()
    d1_common_vals = {key: value for (key, value) in d1.items() if key in intersection_dict.keys()}
    d2_common_vals = {key: value for (key, value) in d2.items() if key in intersection_dict.keys()}

    # for each common key
    for key in intersection_dict:
        # call f on the associated vals in d1 and d2, then assign as common_keys value
        intersection_dict[key] = f(d1_common_vals[key], d2_common_vals[key])


    # DIFFERENCE
    # find all keys unique to d1 or d2, not existing in both
    d1_unique = {key: value for (key, value) in d1.items() if key not in d2.keys()}
    d2_unique = {key: value for (key, value) in d2.items() if key not in d1.keys()}


    # make a new dictionary of those key-value pairs called difference_dict
    d1_unique.update(d2_unique)
    difference_dict = d1_unique
    print(difference_dict)

    print (intersection_dict, difference_dict)
    return (intersection_dict, difference_dict)


d1 = {1:30, 2:20, 3:30, 5:80}
d2 = {1:40, 2:50, 3:60, 4:70, 6:90}
dict_interdiff(d1, d2)
