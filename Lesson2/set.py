# Set - no duplicates

my_set = {10, 20, 30, 40, 40}
print(my_set)

# Add - always add at the start of it
my_set.add(20)
my_set.add(70)
print(my_set)

# Remove - cant remove number that is not in the set
my_set.remove(20)
# my_set.remove(50) # Error
print(my_set)

# Discard - doesn't through an error
my_set.discard(40)
my_set.discard(50)
print(my_set)

# Check if in
if_existing = 10 in my_set
print(if_existing)
if_existing_other = 15 in my_set
print(if_existing_other)

# Union - merge two sets without duplicates
my_new_set = {85, 10, 98}
union_set = my_set.union(my_new_set)
print(union_set)

# Intersection - shared elements in both sets
intersection_set = my_set.intersection(my_new_set)
print(intersection_set)

# Difference - not shared elements
difference_set = my_set.difference(my_new_set)
print(difference_set)
difference_set = my_new_set.difference(my_set)
print(difference_set)

# Symmetric
symmetric_set = my_new_set.symmetric_difference(my_set)
print(symmetric_set)