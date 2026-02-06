import pandas as pd

#Read student.csv file into a Data Frame
studentDataFrame = pd.read_csv("student.csv",delimiter=",")

#Filter students that have the following:
#studytime is greater than or equal to 3
#internet access is equal to 1
#absences are less than or equal to 5
filteredStudentsfromDataFrame = studentDataFrame[
    (studentDataFrame["studytime"]>=3)&
    (studentDataFrame["internet"]==1)&
    (studentDataFrame["absences"]<=5)
]

#Save filtered students to a new file named high_engagement.csv
filteredStudentsfromDataFrame.to_csv("high_engagement.csv",index=False)

#Count how many students have been filtered
FinalnumberofStudents = len(filteredStudentsfromDataFrame)
#Calculate the average grade of the filtered students
averageGrade = filteredStudentsfromDataFrame["grade"].mean()

#Print the results
print(f"Number of students saved: {FinalnumberofStudents}")
print(f"Average grade: {averageGrade:.2f}")