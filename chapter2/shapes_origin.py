import math


# region first_attempt
# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def perimeter(self):
#         raise NotImplementedError("perimeter")

#     def area(self):
#         raise NotImplementedError("area")

# class Square(Shape):
#     def __init__(self, name, side):
#         super().__init__(name)
#         self.side = side

#     def perimeter(self):
#         return 4 * self.side

#     def area(self):
#         return self.side ** 2

# class Circle(Shape):
#     def __init__(self, name, radius):
#         super().__init__(name)
#         self.radius = radius

#     def perimeter(self):
#         return 2 * math.pi * self.radius

#     def area(self):
#         return math.pi * self.radius ** 2

# examples = [Square("square", 10), Circle("circle", 10)]

# for thing in examples:
#     n = thing.name
#     p = thing.perimeter()
#     a = thing.area()

#     print(f"{n},{p},{a}")

# def example():
#     print("in example")

# alias = example
# alias()
# endregion

def shape_density(thing, weight):
    return weight / call(thing, 'area')

def shape_new(name):
    return {
        'name': name,
        '_class': Shape,
    }

Shape = {
    'density': shape_density,
    '_classname': 'shape',
    '_parent': None,
    '_new': shape_new,
}

def square_perimeter(thing):
    return 4 * thing['side']

def square_area(thing):
    return thing['side'] ** 2

def square_larger(thing, size):
    return thing['side'] > size

def square_new(name, side):
    return make(Shape, name) | {
        'side': side,
        '_class': Square
    }

Square = {
    'perimeter': square_perimeter,
    'area': square_area,
    'larger': square_larger,
    '_classname': 'Square',
    '_parent': Shape,
    '_new': square_new,
}

# def square_new(name, side):
#     return {
#         'name': name,
#         'side': side,
#         '_class': Square,
#     }

def call(thing, method_name, *args, **kwargs):
    return thing['_class'][method_name](thing, *args, **kwargs)

def find(thing, method_name):
    cls = thing['_class']

    while cls != None:
        if method_name in cls:
            return cls[method_name]
        else:
            cls = cls['_parent']

    raise NotImplementedError

def make(cls, *args):
    return cls['_new'](*args)

# def call(thing, method_name):
#     return thing['_class'][method_name](thing)

examples = [make(Square,'square1', 10 ), make(Square,'square2', 3 )]
for thing in examples:
    n = thing['name']
    p = call(thing, 'perimeter')
    a = call(thing, 'area')
    is_larger = call(thing, 'larger',10 )
    c = thing['_class']['_classname']
    density = find(thing, 'density')(thing, 10)

    print(f"{n},{p},{a},{c},{is_larger},{density}")

# region spread and vargs
# def show_args(title, *args, **kwargs):
#     print(f"{title} args '{args}' and kwargs '{kwargs}'")

# show_args("nothing")
# show_args("one unnamed argument", 1)
# show_args("one named argument", second="2")
# show_args("one of each", 3, fourth="4")

# show_args("no", 3,4,5,6, second=1, fourth=4)

# def show_spread(left, middle, right):
#     print(f"left {left} middle {middle} right {right}")

# all_in_list = [1, 2, 3]
# show_spread(*all_in_list)

# all_in_dict = {"right": 30, "left": 10, "middle": 20}
# show_spread(**all_in_dict)
# endregion
