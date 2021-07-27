n = int(input("Enter the number of elements: "))
li = []

for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

ele = int(input("Enter the element to count it's occurrences: "))

c = li.count(ele)

print(ele,"has ouccerred", c,"times")