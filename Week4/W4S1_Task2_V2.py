# Original list
color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# IMPORTANT: Always remove the highest index first.
# If we remove index 0 first, all later indices shift left and become wrong.

# Step 1: Remove the element currently at index 5 (Yellow)
color_list.pop(5)

# Step 2: Now the list is shorter. Remove the element at index 4 (Pink)
color_list.pop(4)

# Step 3: Finally remove the element at index 0 (Red)
color_list.pop(0)

print(color_list)   # Output: ['Green', 'White', 'Black']
