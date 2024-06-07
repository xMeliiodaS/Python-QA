# 2 - tuple - cant change it after creating it

my_tuple = (1, 2, 5, 7, 3, 53, 745, 24, 163)
print(my_tuple.index(1))

# Slice in tuple
my_slice = my_tuple[1:4]
print(my_slice)

# Concatenating tuples
my_new_tuple = (10, 20, 30)
concat_tuple = my_tuple + my_new_tuple
print(concat_tuple)

# Repeating tuple
repeating_tuple = concat_tuple * 3
print(repeating_tuple)

# Count in tuple
count = repeating_tuple.count(10)
print(count)

# Index in tuple
my_index = repeating_tuple.index(24)
print(my_index)