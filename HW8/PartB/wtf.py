def decorator(func):
    return func

def some_func():
    pass

#some_func is preserved
some_func = decorator(some_func)
print(some_func)
print(type(some_func))

#some_func becomes an integer
some_func = decorator(2)
print(some_func)
print(type(some_func))



#print(some_func())
#print(type(some_func()))
