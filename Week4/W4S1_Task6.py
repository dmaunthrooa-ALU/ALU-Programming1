
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

#------------Method 1-------------------------------
# Keep an item from list1 only if it also exists in list2
common = [item for item in list1 if item in list2]
print(common)   # [4, 5, 6]

#------------Method 2-------------------------------
# The & operator computes the intersection of two sets
common_set = list(set(list1) & set(list2))
print(common_set)   # [4, 5, 6]  (order may differ)
