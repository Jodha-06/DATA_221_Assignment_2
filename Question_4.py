import pandas as pd

studentDataFrame = pd.read_csv("student.csv",delimiter=",")

filteredStudentsfromDataFrame = studentDataFrame[
    (studentDataFrame["studytime"]>=3)&
    (studentDataFrame["internet"]==1)&
    (studentDataFrame["absences"]<=5)
]

filteredStudentsfromDataFrame.to_csv("high_engagement.csv",index=False)

FinalnumberofStudents = len(filteredStudentsfromDataFrame)
averageGrade = filteredStudentsfromDataFrame["grade"].mean()

print(f"Number of students saved: {FinalnumberofStudents}")
print(f"Average grade: {averageGrade}")