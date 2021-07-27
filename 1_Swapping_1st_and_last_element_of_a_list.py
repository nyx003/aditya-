n = int(input("Enter the number of elements: "))
li = []
for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

f = li[0]
l = li[-1]

li[-1] = f
li[0] = l

print("List after swapping element",li)