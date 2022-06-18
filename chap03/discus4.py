# discus4.py

print("Problem A")
for i in range(1, 11):
  print(i * i, end=" ")
print("\n")

print("Problem B")
for i in [1, 3, 5, 7, 9]:
    print(i, ":", i ** 3, end=", ")
print("\n")

print("Problem C")
x = 2
y = 10
for j in range (0, y, x):
    print(j, end=" ")
print("\n")

print("Problem D")
ans = 0
for i in range(1, 11):
    ans = ans + i * i
    print(i, end=" ")
print(ans)
