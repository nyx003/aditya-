n = int(input("Enter the number of elements: "))
li = []

for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

mul = 1

for i in range(n):
    mul *= li[i]

print("The multiplication of the list is", mul)