import pandas as pd

#Read the crime.csv file into a Data Frame
crimeDataFrame = pd.read_csv("crime.csv",delimiter=",")

#Function that assigns a crime risk level based on the "ViolentCrimesPerPop" value
def assignRiskLevel(ViolentCrimeRatePerPop):
    if ViolentCrimeRatePerPop >=0.50:
        return "High Crime"
    else:
        return "Low Crime"

#New column called "risk"
crimeDataFrame["risk"] = crimeDataFrame["ViolentCrimesPerPop"].apply(assignRiskLevel)

#Group by risk level and calculate the average unemployment rate
groupedCrimeDataByRisk = crimeDataFrame.groupby("risk")["PctUnemployed"].mean()

print(f"Average unemployment rate by crime risk level:\n")

#Average unemployment rate for high crime areas
highCrimeAverage = groupedCrimeDataByRisk["High Crime"]
print(f"For areas with high crime (ViolentCrimesPerPop >= 0.50):")
print(f"Average unemployment rate is: {highCrimeAverage:.2f}\n")

#Average unemployment rate for low crime areas
lowCrimeAverage = groupedCrimeDataByRisk["Low Crime"]
print(f"For areas with low crime (ViolentCrimesPerPop < 0.50):")
print(f"Average unemployment rate is: {lowCrimeAverage:.2f}")
