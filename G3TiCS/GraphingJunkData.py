import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("G3TiCS/pennData500.csv")

#histogram
plt.hist(data["GPA"], edgecolor="purple", color="pink", linewidth=1.2)
plt.xlabel("GPA")
plt.ylabel("# of students")
plt.title("Distribution of GPA in Fake Data Set")
plt.show()

#bar chart
pc = data["Pathway"].value_counts() #ask da panda to count how many times each value appears/occurs
print(pc)
plt.bar(pc.index, pc.values, color="lightcoral", edgecolor="purple")
plt.xlabel("Pathway")
plt.ylabel("# of students")
plt.title("Distribution of Pathways in Fake Data Set")
plt.show()

#bar chart
yc = data["Year"].value_counts()
print(yc)
plt.bar(yc.index, yc.values, color="purple", edgecolor="blue")
plt.xlabel("Year")
plt.ylabel("# of students")
plt.title("Distribution of Years in Fake Data Set")
plt.show()

#pie chart
plt.pie(yc.values)
plt.xlabel("Year")
plt.ylabel("% of students")
plt.title("Distribution of Years in Fake Data Set")
plt.show()

#scatter plot (compare two quantitative variables)
plt.scatter(data["Credits Completed"],data["GPA"])
plt.xlabel("Credits Completed")
plt.ylabel("GPA")
plt.title("Relationship between Credits Completed and GPA")
plt.show()