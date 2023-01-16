#Still working with comparisons but...
def is_even(x: int) -> bool:
    return x % 2 == 0

print(is_even(2))
print(is_even(7))

def is_odd(x: int) -> bool:
    return not is_even(x)

print(is_even(2))
print(is_even(2.9))
print(is_even(7))
print(is_even(5))
print(is_even(16))

def divides(x: int, y: int) -> bool:
   return y % x == 0

print()
print(divides(58,6))

def simple_func(x):
    return(x +30)
    return(x**2)

print(simple_func(4))
