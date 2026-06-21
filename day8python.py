import pandas as pd

students=pd.read_csv("day8python.csv")
print(f"the number of the students is {students.shape[0]}")

students['average'] = (students['math'] + students['science'] + students['english']) / 3
print(f"the student with the highest average is {students.loc[students['average'].idxmax(), 'name']}")

top_students = students.loc[students['average'] > 12]
print(top_students)
top_students.to_csv("top_students.csv", index=False)