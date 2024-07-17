'''find a method to insert all the element of another sequence datatype at particular index in the list. 
 but all the elements must be inserted one by one'''


my_list = [1, 2, 3, 4, 5]

# Sequence to insert
another_sequence = [10, 20, 30]

# Index at which to insert
index = 2

# Insert each element one by one
for element in another_sequence:
    my_list.insert(index, element)
    index += 1  # Increment the index to insert the next element at the correct position

# Print the updated list
print(my_list)