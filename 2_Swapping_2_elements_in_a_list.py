n = int(input("Enter the number of elements: "))
li = []

for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

pos1 = int(input("Enter the 1st position to swap: "))
pos2 = int(input("Enter the 2nd position to swap: "))

li[pos1 - 1], li[pos2 -1] = li[pos2 - 1], li[pos1 -1]

print("The list after swapping is",li)