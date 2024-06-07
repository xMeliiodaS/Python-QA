# Dictionary - (key, value) key is primal
my_dict = {'Name': "Bahaa", "Age": 22, "City": "Dalia"}
print(my_dict)

# Add - update existing value or adding new key and value if it does not exist
my_dict["Age"] = 23
print(my_dict)

my_dict["Gender"] = "Male"
print(my_dict)

# Pop
my_pop = my_dict.pop("Gender")
print(my_pop)
print(my_dict)

# Get - getting the value, if it does not exist it return null (None)
my_get_name = my_dict.get("Name")
my_get_gender = my_dict.get("Gender")
print(my_get_name)
print(my_get_gender)
print(my_dict)

# Key - checks if key exist, not a value
is_existing = "Name" in my_dict
print(is_existing)

# Iteration
for key, value in my_dict.items():
    print(f"{key}: {value}")
print()

# Return Keys and values
key = my_dict.keys()
value = my_dict.values()
print(key)
print(value)