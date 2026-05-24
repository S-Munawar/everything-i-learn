# 5. Identity Operators
# Used to compare the objects, not if they are equal, but if they are actually the SAME object in memory.

print("--- Identity Operators ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 = [1, 2, 3]")
print("list2 = [1, 2, 3]")
print("list3 = list1\n")

print(f"list1 == list2 is {list1 == list2} (Same values)")
print(f"list1 is list2 is {list1 is list2} (Different objects in memory)")
print(f"list1 is list3 is {list1 is list3} (Same object in memory)")
print(f"list1 is not list2 is {list1 is not list2}")
