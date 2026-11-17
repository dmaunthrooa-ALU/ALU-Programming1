color_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Create a brand-new list that keeps only the elements whose index
# is NOT 0, 4 or 5. This avoids the shifting-index problem completely.
new_list = [color_list[i] for i in range(len(color_list)) if i not in (0, 4, 5)]

print(new_list)   # ['Green', 'White', 'Black']
