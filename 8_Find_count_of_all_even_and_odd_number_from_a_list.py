n = int(input("Enter the number of elements: "))
li = []

for i in range(n):
    li.append(int(input("Enter the element: ")))
print("The list is",li)

ecount = 0
ocount = 0

for i in range(n):
    if (li[i] % 2) != 0:
        ocount = ocount + 1
    else:
        ecount = ecount + 1

print("Count of even numbers in the list is", ecount, "and count of odd numbers in the list is", ocount)