from prettytable import PrettyTable 

list=[["stdid","stdname","standard","age","Hindi","English","Maths","science","Computer","Total"],
      ["std101","Ashish Kumar","10th","15","67","89","87","89","90","422"],
      ["std102","Abhishek Kumar","10th","14","85","45","48","90","45","313"],
       ["std103","Aman","10th","15","23","56","78","78","67","302"],
       ["std104","Rahul","10th","14","45","67","45","45","56","258"],
        ["std105","Ruby","10th","13","89","67","89","93","65","403"],
         ["std106","suman","10th","13","90","46","67","67","67","337"],
         ["std107","saurabh","10th","15","45","23","34","45","34","181"],
          ["std108","sumit","10th","14","23","45","67","78","90","303"],
          ["std109","kamlesh","10th","15","45","56","78","99","67","345"],]                                                                                                                                                                                     
         
table = PrettyTable()

# Set the field names (header)
table.field_names = list[0]

# Add rows to the table
for row in list[1:]:
    table.add_row(row)

# Print the table
print(table)





#names of students whose marks is greater than 50 in english

# Index of the English marks in the data
english_index = list[0].index("English")

# Print names of students with English marks greater than 50
for row in list[1:]:
    if int(row[english_index]) > 50:
        print(row[1])




#names of students of top 4 in maths and print their age 
# Index of the Total marks in the data
maths_index = list[0].index("Maths")

# Sort the data based on Total marks in descending order
sorted_data = sorted(list[1:], key=lambda x: int(x[maths_index]), reverse=True)

# Get the top 4 students
top_4_students = sorted_data[:4]

# Print the names and ages of the top 4 students
for student in top_4_students:
    name = student[1]
    age = student[3]
    print(f"Name: {name}, Age: {age}")        



#bottom 4 scorer in computer
# Index of the Computer marks in the data
computer_index = data[0].index("Computer")

# Sort the data based on Computer marks in ascending order
sorted_data = sorted(data[1:], key=lambda x: int(x[computer_index]))

# Get the bottom 4 students
bottom_4_students = sorted_data[:4]

# Print the names and ages of the bottom 4 students
print("\nBottom 4 students in Computer and their ages:")
for student in bottom_4_students:
    name = student[1]
    age = student[3]
    print(f"Name: {name}, Age: {age}")



