# discus6.py
# magic formula - a = (a//b)(b) + (a%b)
# Example
a, b = -10, 3

x = a//b
y, z = x * b, a%b

print(f'(a//b) * b is {y} and (a%b) is {z}.')
print(f'so, (a//b) * b + (a%b) is {y+z}.')

print()
print('a) ', -10//3)

print()
print('b) ', -10%3)

print()
print('c) ', 10//-3)

print()
print('d) ', 10%-3)

print()
print('e) ', -10/-3)




