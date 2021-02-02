numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]

print(new_numbers)



name = "Jean-Baptiste"
new_list = [letter for letter in name]

print(new_list)



new_range = [n*2 for n in range(1, 5)]

print(new_range)



names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
long_names = [name.upper() for name in names if len(name) > 5]

print(short_names)
print(long_names)



import random

student_score = {name: random.randint(0, 100) for name in names}

print(student_score)

passed_students = {name: score for (name, score) in student_score.items() if score > 50}

print(passed_students)



import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56,76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row)