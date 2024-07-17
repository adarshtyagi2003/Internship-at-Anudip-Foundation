import tabulate


student_records = {
    "1": {"stdid": 1, "stdname": "Alice", "age": 14, "standard" :" 10th" , "hindi": 78, "english": 88, "maths": 95, "science": 89, "computer": 90, "total": 440},
    "2": {"stdid": 2, "stdname": "Bob", "age": 15,"standard" :" 10th" , "hindi": 82, "english": 79, "maths": 85, "science": 88, "computer": 92, "total": 426},
    "3": {"stdid": 3, "stdname": "Charlie", "age": 14, "standard" :" 10th" ,"hindi": 90, "english": 85, "maths": 88, "science": 92, "computer": 91, "total": 446},
    "4": {"stdid": 4, "stdname": "David", "age": 15, "standard" :" 10th" ,"hindi": 70, "english": 80, "maths": 78, "science": 85, "computer": 87, "total": 400},
    "5": {"stdid": 5, "stdname": "Eve", "age": 14,"standard" :" 10th" , "hindi": 95, "english": 89, "maths": 92, "science": 94, "computer": 96, "total": 466},
    "6": {"stdid": 6, "stdname": "Frank", "age": 15,"standard" :" 10th" , "hindi": 60, "english": 70, "maths": 68, "science": 75, "computer": 80, "total": 353},
    "7": {"stdid": 7, "stdname": "Grace", "age": 14, "standard" :" 10th" ,"hindi": 85, "english": 87, "maths": 90, "science": 88, "computer": 89, "total": 439},
    "8": {"stdid": 8, "stdname": "Heidi", "age": 15, "standard" :" 10th" ,"hindi": 88, "english": 90, "maths": 85, "science": 91, "computer": 93, "total": 447},
    "9": {"stdid": 9, "stdname": "Ivan", "age": 14,"standard" :" 10th" , "hindi": 72, "english": 75, "maths": 78, "science": 80, "computer": 82, "total": 387},
    "10": {"stdid": 10, "stdname": "Judy", "age": 15, "standard" :" 10th" ,"hindi": 89, "english": 92, "maths": 91, "science": 90, "computer": 94, "total": 456}
}

list1=list(student_records.keys())
list2=list(student_records.values())

table_data = []
for value in list2:
    row = [value["stdid"],value["stdname"], value["standard"], value["age"], value["hindi"], value["english"], value["maths"], value["science"], value["computer"], value["total"]]
    table_data.append(row)

# Print the table
print(tabulate.tabulate(table_data, headers=["Stdid","Name", "Standard", "Age", "Hindi", "English", "Maths", "Science", "Computer", "Total"]))






#display the name of students whose marks in english is greater than 50 
# Find students with English marks greater than 50
students_above_50_english = [value["stdname"] for value in student_records.values() if value["english"] > 50]

# Print the names of students
print("\nStudents with English marks greater than 50:")
for student in students_above_50_english:
    print(student)






# Sort students by their Maths scores in descending order and get the top four scorers
top_four_maths = sorted(student_records.values(), key=lambda x: x["maths"], reverse=True)[:4]

# Print the names and ages of the top four Maths scorers
print("\nTop Four Scorers in Maths:")
for student in top_four_maths:
    print(f"Name: {student['stdname']}, Age: {student['age']}")



#bottom 4 scorer in computer
bottom_four_computer = sorted(student_records.values(), key=lambda x: x["computer"], )[:4]
print('\nbottom 4 scorer in computer')
for student in bottom_four_computer:
    print(f"Name: {student['stdname']}, Age: {student['age']}")
