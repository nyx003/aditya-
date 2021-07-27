n = int(input("Enter the number of elements: "))
li = []

for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

odd = []

for i in range(n):
    if (li[i] % 2) != 0:
        odd.append(li[i])

print("The list of odd numbers from the primary list is",odd)