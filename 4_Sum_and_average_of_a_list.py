n = int(input("Enter the number of elements: "))
li = []

for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

sum = 0

for i in range(n):
    sum += li[i]

average = sum/n

print("The sum of the list is", sum)
print("The average of the list is", average)