import pandas as pd

scores = pd.DataFrame(
    [
        [85, 91, 78, 92],
        [88, 76, 95, 89],
        [90, 87, 84, 93]
    ],
    index=["Alex", "Sam", "Jordan"],
    columns=["Assignment 1", "Assignment 2",
             "Assignment 3", "Assignment 4"]
)
print(scores)

data = pd.read_csv("G3TiCS/pennData500.csv")

print("\nHead of the DataFrame:")
print(data.head())
print("\nTail of the DataFrame:")
print(data.tail())
print("\nShape of the DataFrame:")
print(data.shape)
print("\nNames of the columns:")
print(data.columns)
print("\nData types of the columns:")
print(data.dtypes)
print("\nDescribe function output:")
print(data.describe())
print("\n")
print(data["GPA"].mean())
print(data["GPA"].median())
print(data["GPA"].min())
print(data["GPA"].max())
