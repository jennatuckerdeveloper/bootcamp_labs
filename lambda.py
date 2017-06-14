#lambda {var}: {cdoe}

def add_two(x, y):
    return x + y

add_two_l = lambda x, y: x + y

print(add_two_l(5, 5))

print(add_two_l(10, 11))

numbers = list(range(1, 20))
def evens(num):
    return num % 2 == 0

print(list(filter(evens, numbers)))

print(list(filter(lambda num: num % 2 == 0, numbers)))

#filter will only give back the thing that's true

portland_temp_june_week_1 = [66, 66, 62, 61, 63, 71, 67]
portland_temp_june_week_2 = [62, 58, 56, 62, 57, 57, 53]

lambda x: x if x % 2 == 0 else 0

#lambda's work better for one time, not with if/else