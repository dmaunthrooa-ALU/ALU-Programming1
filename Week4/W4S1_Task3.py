# ----- Method 1: extend() – modifies the original list -----
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# extend() takes each element of list2 and adds it individually to list1
list1.extend(list2)
print(list1)          # [1, 2, 3, 4, 5, 6]

# ----- Method 2: + operator – creates a brand-new list -----
list3 = [1, 2, 3]
list4 = [4, 5, 6]
combined = list3 + list4   # The original lists stay unchanged
print(combined)       # [1, 2, 3, 4, 5, 6]

# ----- Method 3: append()
list5 = [1, 2, 3]
list5.append(4)
list5.append(5)
list5.append(6)
print(list5)          # [1, 2, 3, [4, 5, 6]]  ← nested list
