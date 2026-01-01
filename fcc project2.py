import pandas as pd
df = pd.read_csv("adult.csv")
df.shape

# Task 1
group = df["race"].value_counts()
ser = pd.Series(group)
print("The number of people in each race are: ")
print(ser)

# Task 2
df["sex"] = df["sex"].str.lstrip()
df["education"] = df["education"].str.lstrip()
df["salary"] = df["salary"].str.lstrip()
male_avg = df[df["sex"] == "Male"]["age"].mean().astype("int")
print("The average age of men is:", male_avg)

# Task 3
bach_deg = df[df["education"] == "Bachelors"]["age"].shape[0]
per = (bach_deg/32560)*100
print("Percentage of people having bachelor degree: %.2f%%" % per)

# Task 4
a = df[(((df["education"] == "Bachelors") | (df["education"] == "Masters") | (
    df["education"] == "Doctorate")) & (df["salary"] == ">50K"))].shape[0]
per = ((a/32560)*100)
print("Percentage of People having higher education and earning more than 50K: %.2f%%" % per)

# Task 5
a = df[(((df["education"] != "Bachelors") & (df["education"] != "Masters") & (
    df["education"] != "Doctorate")) & (df["salary"] == ">50K"))].shape[0]
per = ((a/32560)*100)
print("Percentage of People having not higher education and earning more than 50K: %.2f%%" % per)

# Task 6
print("Minimum number of hour(s) a person work per week:", end=" ")
print(df["hours-per-week"].min())

# Task 7
print("Number of people who work minimum number of hours per week and have salary more than 50k:", end=" ")
print(((df["hours-per-week"] == df["hours-per-week"].min())
      & (df["salary"] == ">50K")).sum())

# Task 8
s = pd.DataFrame((df[df["salary"] == ">50K"])["native-country"].value_counts())
print("country having the highest percentage of people that earn >50K: ", end="")
print(s.index[0])
per = (float(s.iloc[0])/32560)*100
print("Percentage: %.2f%%" % per)

# Task 9
ind_occup = df[(df["salary"] == ">50K") & (
    df["native-country"] == " India")]["occupation"].value_counts()
print("The most popular occupation for those who earn >50K in India:",
      ind_occup.index[0])
