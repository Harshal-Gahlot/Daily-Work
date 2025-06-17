import pandas as pd

df = pd.read_csv('job_applicants_dataset.csv')
# print(df.head(10))

genderDf = df.isin({"Gender": [0, "Male"]})

print("\nTotal Humans applicants:", len(df))
print("Total Males applicants:", genderDf["Gender"].sum())
print("Total Females applicants:", len(df) - genderDf["Gender"].sum())

maleDf = df[(df["Gender"] == "Male") & (df["Hired"] == 1)]
maleLen = len(maleDf)
print("\nTotal Male applicants hired:", maleLen)

femaleDf = df[(df["Gender"] == "Female") & (df["Hired"] == 1)]
femaleLen = len(femaleDf)
print("Total Female applicants hired:", femaleLen)

print(f"female to male  hiring Ratio- 1:{maleLen/femaleLen:.2f}")

print("\nSince male get hired over 5 times than female, thus hiring was biased towards male applicants.")