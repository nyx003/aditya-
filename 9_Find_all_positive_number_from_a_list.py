n = int(input("Enter the number of elements: "))
li = []

for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

positive = []

for i in range(n):
    if li[i] > 0:
        positive.append(li[i])

print("The list of positive numbers from the primary list is",positive)