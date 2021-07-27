n = int(input("Enter the number of elements: "))
li = []

for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

even = []

for i in range(n):
    if (li[i] % 2) == 0:
        even.append(li[i])

print("The list of even numbers from the primary list is",even)