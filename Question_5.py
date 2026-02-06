import pandas as pd

#Read the student.csv file to a Data Frame
studentDataFrame = pd.read_csv("student.csv",delimiter=",")

#Function that assigns a "grade band" based on a students grade
def assignGradeBand(grade):
    if grade <=9:
        return "Low"
    elif 10 <= grade <= 14:
        return "Medium"
    else:
        return "High"

#New column called "grade band"
studentDataFrame["grade_band"] = studentDataFrame["grade"].apply(assignGradeBand)

#Group by "grade band" and count how many students are in each band
groupedNumber = studentDataFrame.groupby("grade_band")["grade"].count()
#Average number of absences for each band
groupedAverageAbsences = studentDataFrame.groupby("grade_band")["absences"].mean()
#How many students in each band have internet access
groupedInternetSum = studentDataFrame.groupby("grade_band")["internet"].sum()

#Stores the total number of students in each band
totalStudentsinBand = groupedNumber

#Calculates percentage of students with internet access in each band
groupedInternetPercentage = (groupedInternetSum / totalStudentsinBand) * 100

#Creates a summary table
groupedSummaryTable = pd.DataFrame({
    "grade_band": groupedNumber.index,
    "number_of_students": groupedNumber.values,
    "average_absences": groupedAverageAbsences.values,
    "percentage_with_internet": groupedInternetPercentage.values
})

#Save the summary table to a new file called "student_bands.csv"
groupedSummaryTable.to_csv("student_bands.csv",index=False)

print(groupedSummaryTable)