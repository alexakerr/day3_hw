# Problem One - Task One
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
sorted_grades = sorted(grades, reverse=True)
print("Sorted grades in descending order:", sorted_grades)

# Problem One - Task Two
average_grade = sum(grades) / len(grades)
print("Average grade:", average_grade)

# Problem One - Task Three
grades_with_failed = ["Failed" if grade < 80 else grade for grade in grades]
print("Grades with failed:", grades_with_failed)



# Problem Two - Task One
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

common_students = [student for student in submitted if student in attended]
print("Students who submitted assignments and attended the class:", common_students)

# Problem Two - Task Two
are_identical = sorted(submitted) == sorted(attended)
print("Are the two lists identical in terms of their content?", are_identical)

# Problem Two - Task Three
attended = [student for student in attended if student in submitted]
print("Attended list after removing students who didn't submit assignments:", attended)



# Probem Three - Task One
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
second_week_temperatures = temperatures[7:14]
print(second_week_temperatures)

# Problem Three - Task Two
temperatures_above_100 = [temp for temp in temperatures if temp > 100]
print(temperatures_above_100)

# Problem Three - Task Three
reversed_temperatures = temperatures[::-1]
reversed_temperatures_subset = reversed_temperatures[4:10]
print(reversed_temperatures_subset)



# Problem Four - Task One
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

for student, grade, activity in zip(students, grades, activities):
    if grade < 80:
        print(f"{student}, {grade}, {activity}")

# Problem Four - Task Two
students_approved = [student for student, grade in zip(students, grades) if grade >= 80]

# Problem Four - Task Three
print("Students approved for the event:", students_approved)











