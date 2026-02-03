import pandas as pd

crimeDataFrame = pd.read_csv("crime.csv",delimiter=",")

def assignRiskLevel(ViolentCrimeRatePerPop):
    if ViolentCrimeRatePerPop >=0.50:
        return "High Crime"
    else:
        return "Low Crime"

crimeDataFrame["risk"] = crimeDataFrame["ViolentCrimesPerPop"].apply(assignRiskLevel)

groupedCrimeDataByRisk = crimeDataFrame.groupby("risk")["PctUnemployed"].mean()

print("Average unemployment rate by crime risk level:")
print("")
highCrimeAverage = groupedCrimeDataByRisk["High Crime"]
print(f"For areas with high crime (ViolentCrimesPerPop >= 0.50):")
print(f"Average unemployment rate is: {highCrimeAverage:.2f}")
print("")
lowCrimeAverage = groupedCrimeDataByRisk["Low Crime"]
print(f"For areas with low crime (ViolentCrimesPerPop < 0.50):")
print(f"Average unemployment rate is: {lowCrimeAverage:.2f}")
