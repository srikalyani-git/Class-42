
students = [["John Doe", "001", "Year 10"], ["Jane Smith", "002", "Year 11"], ["Emily Davis", "003", "Year 12"], ["Michael Brown", "004", "Year 10"], ["Sarah Wilson", "005", "Year 11"]]
student_info = {"Name": [], "ID": [], "Grade": []}
for i in range(len(students)):
    student_info["Name"].append(students[i][0])
    student_info["ID"].append(students[i][1])
    student_info["Grade"].append(students[i][2])

print("Student Information:", student_info)