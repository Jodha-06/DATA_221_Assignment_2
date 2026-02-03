import pandas as pd

studentDataFrame = pd.read_csv("student.csv",delimiter=",")

def assignGradeBand(grade):
    if grade <=9:
        return "Low"
    elif 10 <= grade <= 14:
        return "Medium"
    else:
        return "High"

studentDataFrame["grade_band"] = studentDataFrame["grade"].apply(assignGradeBand)

groupedNumber = studentDataFrame.groupby("grade_band")["grade"].count()
groupedAverageAbsences = studentDataFrame.groupby("grade_band")["absences"].mean()
groupedInternetSum = studentDataFrame.groupby("grade_band")["internet"].sum()

totalStudentsinBand = groupedNumber

groupedInternetPercentage = (groupedInternetSum / totalStudentsinBand) * 100

groupedSummaryTable = pd.DataFrame({
    "grade_band": groupedNumber.index,
    "number_of_students": groupedNumber.values,
    "average_absences": groupedAverageAbsences.values,
    "percentage_with_internet": groupedInternetPercentage.values
})

groupedSummaryTable.to_csv("student_bands.csv",index=False)

print(groupedSummaryTable)