
class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print("call method executed before function {}".format(self.original_function.__name__))
        return self.original_function(*args,*kwargs)

@decorator_class
def display():
    print("Hi!")

@decorator_class
def display_info(name, age):
    print("name : {}, age : {}".format(name, age))


display()

display_info("Dhananjay", 36)
