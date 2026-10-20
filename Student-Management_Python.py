student = ["Arun", "priya", "Vasu", "john", "Kumar"]

print("\n----------adding student to the python course----------------")
student.append("Rahul")
print(student)

print("\n----------------------sneha joins the course-----------------")
student.insert(2,"sneha")
print(student)

print("\n------------------adding some more students-------------------")
student.extend(["David", "Meena", "Ravi"])
print(student)

print("\n------------------remove kumar from the list-------------------")
student.remove("Kumar")
print(student)

print("\n------------------removing ravi from the list--------------------")
Removed_stu = student.pop()
print(Removed_stu)

print("\n-------------------Finding index for vasu-----------------------")
print(student.index("Vasu"))

print("\n--------------------count function--------------------------------")
student.append("priya")
print(student.count("priya"))

print("\n ------------------------sorting students-------------------------")
student.sort()
print(student)

print("\n-----------------------reversing the sorted students----------------")
student.reverse()
print(student)

print("\n--------------------------Taking the copy of students------------------")
New_list = student.copy()
print(New_list)

print("\n------------------------------printing the length of the students-----------")
print(len(student))

print("\n--------------------Finding in the list or not----------------------------")
if "Meena" in student:
    print("Meena is in the student list")
else:
    print("Meena is not in the list")

print("\n----------------------Finding Karthick is in the list or not---------------------")

if "Karthick" not in student:
    print("Karthick is not in the student list")
else:
    print("Karthick is in the list")

print("\n---------------------------indexing------------------------------------")
print(student[2])
print("\n---------------------------slicing--------------------------------------")
print(student[2:6:2])
print("\n---------------------------clearing student list------------------------")
student.clear()
print(student)
