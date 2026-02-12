# WAP to perform the implement the following operations on following list
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print("List Concatenation",list1+list2)
del list1[3]
print("List1 after remove",list1)
list1.append("java")
print("List1 after add",list1)
list2[3]=11
print("List2 after update",list2)

for i in range(4):
    print("Welcome to Marwadi University")

print(len(list2))
print("list1[-2]:", list1[-2])
print("list2[1:3]:", list2[1:3])
print("list1[-1:-3]:", list1[-1:-3])

print(max(list2))
print(min(list2))

list2.insert(2,100)
print(list2)

list3 = [20, 30, 40]
list2.extend(list3)
print("After extend:", list2)