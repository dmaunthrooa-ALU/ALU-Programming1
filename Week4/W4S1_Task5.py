
#------------Method 1-------------------------------
numbers_list1 = [1, 2, 3, 2, 4, 3, 5, 1, 6]

# Convert to a set (automatically removes duplicates), then back to a list
unique_list = list(set(numbers_list1))
print(unique_list)   # Order is NOT guaranteed


#------------Method 2-------------------------------
numbers_list2 = [1, 2, 3, 2, 4, 3, 5, 1, 6]

# Create an empty list that will hold the unique values
unique_ordered = []

# Walk through the original list one item at a time
for item in numbers_list2:
    # Only add the item if we have not already seen it
    if item not in unique_ordered:
        unique_ordered.append(item)

print(unique_ordered)   # [1, 2, 3, 4, 5, 6]  – order is preserved

#------------Method 3-------------------------------
# dict.fromkeys() keeps insertion order and removes duplicates
numbers_list3 = [1, 2, 3, 2, 4, 3, 5, 1, 6]
unique_ordered = list(dict.fromkeys(numbers_list3))
print(unique_ordered)
