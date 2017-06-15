#Decorator: a funciton that modifies another function.

def greeting():
    print("Hello")

hey = greeting

hey()

greeting()

del greeting

hey()

#We can assign a function to a variable and decide when to call it.

def hello():
    def world():
        print(' World!')
    world()
    print('Hello!')

hello()

def hello():
    def world():
        return ' World!'
    print('Hello {}'.format(world()))

hello()

def b():
    print('Thanks for calling!')

def a(function):
    print('I am calling {}'.format(function.__name__))
    function()

a(b)

#Decorator

def my_decorator(function):
    def wrapper(name):
        return 'Hello {}'.format(name)
    return wrapper

@my_decorator
def greet(name):
    return name

print(greet('Chris'))

def strong_decorator(function):
    def wrapper(hmtl):
        return '<strong>{}</strong>'.format(hmtl)
    return wrapper

@strong_decorator
def title(text):
    return text

print(title('I like pie.'))
