

def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Calling decorator function before calling original function {}".format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_function


@decorator_function
def display():
    print("Hi!")

@decorator_function
def display_info(name, age):
    print("Name : {}, Age : {}".format(name, age))

display()
display_info("Dhananjay", 36)
