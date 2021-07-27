n = int(input("Enter the number of elements: "))
li = []

for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

negative = []

for i in range(n):
    if li[i] < 0:
        negative.append(li[i])

print("The list of negative numbers from the primary list is",negative)