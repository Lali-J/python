import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("G3TiCS/pennData500.csv")

#histogram
plt.hist(data["GPA"], edgecolor="yellow", color="pink", linewidth=1.2)
plt.xlabel("GPA")
plt.ylabel("# of students")
plt.title("Distribution of GPA in Fake Data Set")
plt.show()