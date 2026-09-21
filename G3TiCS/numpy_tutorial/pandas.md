# Topics in Computer Science
## Data Science — Introduction to Pandas

### Driving Question
How can we use Pandas to organize and analyze real-world data?

---

## Before You Begin

Last class, you worked with NumPy arrays.

You created a 2D array similar to:

```python
import numpy as np

scores = np.array([
    [85, 91, 78, 92],
    [88, 76, 95, 89],
    [90, 87, 84, 93]
])
```

Think about:
- What does each row represent?
- What does each column represent?
- How do you know?
The problem is that the array itself doesn't tell us.

Today we're going to look at a Python library designed to make
real-world tabular data easier to work with.


## Part 1 — Meet Pandas
Pandas is a Python library used for working with datasets.

You must first install pandas

Open Terminal and type in
```bash
pip3 install pandas
```

Import it using:
```python
import pandas as pd
```

The primary data structure we will use is called a DataFrame.

## Part 2: Your first Dataframe

Run the following code:

```python

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

```

#### Question 1
How is this DataFrame similar to the NumPy array you created last class?
* Your answer: It has the same basic information of there is three students and there is four assignments that hold their scores for each one

#### Question 2
How is it different?
* Your answer: It labled both axes to create a cleaner way to view the code

## Part 3 — Reading a CSV

[Download Data Here](https://github.com/marsh135/python/blob/main/G3TiCS/pennData500.csv)

```python
data = pd.read_csv("pennData500.csv")
```

### Questions:
- What is a DataFrame?
    - A two-dimentional data structure that orgainzes in rows and columns
- How is it similar to the 2D NumPy array you worked with?
    - How it orgainzes the data given
- What's different?
    - The amount and details of the information
- Why are column names useful?
    - It makes the data easy to read for anyone
## Part 4: Looking at the DataFrame
```python
print(data.head())
print(data.tail())
print(data.shape)
print(data.columns)
print(data.dtypes)
```

### Questions:
- What does .head() do?
    - It shows the first pieces of information at the top of the set
- What does .tail() do?
    - It shows the last pieces of information at the bottom
- What is the shape of this data?
    - It has 500 rows and 7 columns
-  What is the result of .columns?
    - It tells you what each column is labeled as
- What is the result of .dtype?
    - It tells you the type of data type in the array

## Describe
```python
print(data.describe())
```

### Questions:
- What does .describe() do?
    - It does a lot!! It tells you the count, mean, std, min, 25%, 50%, 70%, and max for compatable columns.
## Statistics
```python
print(data["COLUMN_NAME"].mean())
print(data["COLUMN_NAME"].median())
print(data["COLUMN_NAME"].min())
print(data["COLUMN_NAME"].max())
```

Replace "COLUMN_NAME" with a column name from the data and run the code above


### Questions:
- Which column did you choose?
    - I chose column GPA
- What is the mean?
    - 2.33026521042084
- What is the median?
    - 2.38
- What is the minimum value?
    - 0.31
- What is the maximum value?
    - 4.3
- In your own words, what do these statistics tell you about the data?
    - There is a very wide range of how good or bad the grades are at this school but overall it seems really negative

## Part 5: Selecting Data

One advantage of a Pandas DataFrame is that we can select specific columns from a large dataset.

To display one column:

```python
print(data["COLUMN_NAME"])
```

Replace `"COLUMN_NAME"` with the name of one of the columns in the Penn dataset.

To display multiple columns:

```
print(data[["COLUMN_1", "COLUMN_2"]])
```

Replace `"COLUMN_1"` and `"COLUMN_2"` with two columns from the dataset.

### Questions:
- Which column did you select first?
    - Year
- What type of data does that column contain?
    - Tells me what year they are currently in
- Which two columns did you select together?
    - Year and their Pathway
- Why might it be useful to look at only a few columns instead of the entire DataFrame?
    - It could be really useful if you are trying to find a correlation between them or need both pieces of information without trying to get overwhelmed

## Part 6: Filtering Data

Pandas can also select only the rows that meet a certain condition.

For example:

```python
filtered_data = data[data["COLUMN_NAME"] > 50]

print(filtered_data)
```

This code tells Pandas:

"Give me only the rows where COLUMN_NAME has a value greater than 50."

You will need to replace `"COLUMN_NAME"` with the name of a **quantitative** column from the Penn dataset.

You may also need to change `50` to a value that makes sense for the column you selected.

### Try It:

Create a filter using a numerical column from the Penn dataset.

```python
filtered_data = data[data["________________"] > ______]

print(filtered_data)
```

### Questions:
- Which column did you filter?
    - The GPA
- What condition did you use?
    - If the student's GPA was higher than a 4.0
- How many rows appear to meet your condition?
    - 51 rows
- In your own words, explain what your filter asked Pandas to find.
    - Basically look in the GPA column and tell me which rows have a GPA higher than 4.0 and tell me the rest of their information

## Part 7: Filtering Qualitative Data

We can also filter using qualitative data.

Instead of asking whether a number is greater than or less than something, we can ask whether a value is equal to something.

Example:

```python
filtered_data = data[data["COLUMN_NAME"] == "VALUE"]

print(filtered_data)
```

Notice the difference:

```python
> 50
```

asks a numerical question.

While:

```python
== "VALUE"
```

asks whether something is equal to a specific value.

### Try It:

Find a qualitative column in the Penn dataset.

Create a filter that displays only rows containing one particular value from that column.

```python
filtered_data = data[data["________________"] == "________________"]

print(filtered_data)
```

### Questions:
- Which qualitative variable did you use?
    - Year
- What value did you search for?
    - If they are on their victory lap year
- What does the resulting DataFrame contain?
    - There are a 104 students who are on their Victory lap year
- Why do we use `==` instead of `=` when checking whether two values are equal?
    - To compare if the years match rather than setting

## Part 8: Combining Selection and Filtering

We can combine what we have learned.

First, filter the data:

```python
filtered_data = data[data["COLUMN_NAME"] > 50]
```

Then select only the columns we want to see:

```python
print(filtered_data[["COLUMN_1", "COLUMN_2"]])
```

Instead of displaying every variable for every matching observation, Pandas will now display only the information we requested.

### Your Turn:

Create your own example that:

- Filters the dataset using a condition  
- Displays at least two columns from the filtered data  

Paste or write your completed code below:

```python
filtered_data = data[data["GPA"] > 4.0]
print(filtered_data[["GPA", "Year"]])
```

### Questions:
- What question were you trying to answer?
    - Does year correlate with how well your grades are
- What did your code find?
    - No absoultely it does not and there are a ton of students from varying grades that have a GPA higher than 4.0
- Did the result match what you expected? Explain.
    - No because there was a good mix of all the grades including victory lap. There wasn't any that stood out as having more than the other grades

## Part 9: Data Detective

Now it is time to put everything together.

For this section, you will receive **less example code**.

Use what you have learned about Pandas to investigate the Penn dataset.

You may use:

```python
data.head()
data.tail()
data.shape
data.columns
data.dtypes
data.describe()
```

You may also use:

```python
data["COLUMN_NAME"]
data["COLUMN_NAME"].mean()
data["COLUMN_NAME"].median()
data["COLUMN_NAME"].min()
data["COLUMN_NAME"].max()
```

And filtering:

```python
data[data["COLUMN_NAME"] > VALUE]
data[data["COLUMN_NAME"] < VALUE]
data[data["COLUMN_NAME"] == "VALUE"]
```

### Challenge 1

How many **rows** and **columns** are in the Penn dataset?
* There are 500 rows and 6 Columns

Write the Pandas command you used and your answer.
```python
print(data.shape)
```

### Challenge 2

Choose one quantitative variable. 
- My quantitative variable was Credits Completed

Determine its:

- Mean 
    - 30.647295
- Median  
    - 32.0
- Minimum 
    - 0
- Maximum
    - 60

What does this information tell you about that variable?
- This school has a very large variety of students effort but overall most are in the 30s range

### Challenge 3

Create a filter that returns only a portion of the dataset.

Your filter must answer a question that you can describe in plain English.

For example:

"How many observations have a value greater than _____?"

Do not use this exact question. Create your own.

Write:

- Your question  
    - How many students are interested in the Computer Science Pathway?
- Your Python code  
``` python
fd3 = data[(data["Pathway"] == "Computer Science")]
print(fd3)
```
- What you discovered
    - Out of 500 students only 42 of them want to proceed with Computer Science

### Challenge 4

Choose two variables that you think might be interesting to examine together.

Display only those two columns.

### Questions:
- Which variables did you choose?
    - Who chose the Computer Science pathway and if their grades are higher than a 3.2
- Why did you choose them?
    - I wanted to see what majority of computer science have a good GPA
- Do you notice anything interesting?
    - Out of 42 students only 15 have a GPA higher than 3.2
- What would you want to investigate further?
    - What grades they are in to see if its easier to be in a certain grade in computer science to get help with your GPA

## Part 10: Ask Your Own Question

This is the most important part of today's assignment.

Data scientists do not just run commands.

They use data to **answer questions**.

Write one question about Penn that you believe this dataset can answer.

### My Question:

Your question: Are all the current seniors set at an acceptable GPA and have enough credit in order to graduate?

### My Code:

Write the Pandas code necessary to help answer your question.

```python

fd5 = data[(data["Year"] == "Senior") & (data["Credits Completed"] <20) | (data["Year"] == "Senior") & (data["GPA"] < 2.0)]
print(fd5[["Name", "Credits Completed", "GPA", "Year"]])

```

### My Result:

What did your program find?
- There are 61 seniors that might have to take a Victory lap unless help is given to them
### What Does It Mean?

Explain your result in a complete sentence.
- Currently 61 seniors either have a GPA less than 2.0 or they have less than 20 credits completed. So these students need a lil extra help or push

Do not simply write the number produced by Python.

For example, instead of:

**"72.4"**

write something like:

**"The average value of ______ in this dataset is 72.4."**

## Part 11: What CAN'T the Data Tell Us?

A dataset can only answer questions about the information it contains.

Write one interesting question about Penn that **cannot** be answered using this dataset.

### Question:

What would you like to know?
- What are the characters like of each student. Are they good or bad or just kinda there? 

### Missing Data:

What additional variable or data would need to be collected to answer your question?
- Number of disaplines for each student such as how many dententions or referals they have recived

## Final Reflection

Answer each question in 1–3 complete sentences.

### 1. NumPy vs. Pandas

What is one major difference you noticed between working with a NumPy array and working with a Pandas DataFrame?
- Pandas DataFrames keep information a lot cleaner and easier to read to just about anybody. Pandas is pretty fun to write the data but panda is better to analyze it.

### 2. DataFrames

Why might a DataFrame be more useful than a basic 2D array when working with a large real-world dataset?
- You can separate the information so you can look at specific ones that meet a requirement or certain clumps of information

### 3. Data Science

Return to today's Driving Question:

**How can we use Pandas to organize and analyze real-world data?**
- We can use it to separate data, find middles, and analyze it to tell us certain details such as x relates to y. Just like how I analyzed it to tell me if we have a lot of computer science students then further to see if they are a good student academically.

Answer the question using something you did during today's activity as an example.

## Before You Are Finished

Make sure you have:

- [X] Installed and imported Pandas  
- [X] Created your first DataFrame  
- [X] Loaded `pennData500.csv`  
- [X] Used `.head()` and `.tail()`  
- [X] Examined the shape, columns, and data types  
- [X] Used `.describe()`  
- [X] Calculated summary statistics  
- [X] Selected individual columns  
- [X] Filtered quantitative data  
- [X] Filtered qualitative data  
- [X] Completed the Data Detective challenges  
- [X] Created and answered your own data question  
- [X] Identified a question the dataset cannot answer  
- [X] Completed the final reflection  

## If You Finish Early

Continue exploring the Penn dataset.

Try to discover something interesting that was **not specifically asked for in this assignment**.

You may use the Pandas documentation or search for additional Pandas commands.

Some things you might investigate:

- How can you count how many times each value appears?  
- How can you sort a DataFrame?  
- How can you find the standard deviation of a column?  
- How can you find only the rows where **two conditions** are true?

Document anything new that you discover.

Be prepared to show me what you figured out when I return.