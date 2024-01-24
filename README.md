# NYC Public School SAT Performance Analysis

## Overview

This project focuses on analyzing the SAT performance of New York City (NYC) public schools, utilizing the dataset "schools.csv". The SATs, a crucial component of the American high school experience, assess literacy, numeracy, and writing skills. The analysis aims to provide insights into school performance, assisting various stakeholders such as policy and education professionals, researchers, government bodies, and parents making informed decisions about their children's education.

## Key Questions

### 1. Identifying Top Math-Performing Schools

- **Objective:** Create a pandas DataFrame named "best_math_schools" containing the "school_name" and "average_math" score for schools where the math results are at least 80% of the maximum possible score.
  
- **Code Snippet:**
  ```python
  import pandas as pd
  import matplotlib.pyplot as plt

  schools = pd.read_csv("schools.csv")

  Threshhold = 0.8 * 800
  best_math_schools = schools.loc[schools['average_math'] >= Threshhold,     ['school_name', 'average_math']]
  best_math_schools = best_math_schools.sort_values(by='average_math',   ascending=True)
  fig = plt.figure(figsize=(10,6))
  plt.barh(y=best_math_schools['school_name'],width=best_math_schools['average_math'])
  plt.xlabel("Math Scores")
  plt.title("Top 10 Math Performing Schools")
  plt.yticks(fontsize=10)
  plt.show()
  ```
### Top Math-Performing Schools Horizontal Bar Chart:
<img width="998" alt="Screenshot 2024-01-23 at 11 40 20 PM" src="https://github.com/Gregory204/NYC-SAT-Insights/assets/131078905/f50fe8a6-bdbd-456e-8fb5-268406e330e8">

### Top Math-Performing Schools Table:

### SQL Table:
<img width="353" alt="Screenshot 2024-01-24 at 12 36 13 AM" src="https://github.com/Gregory204/NYC-SAT-Insights/assets/131078905/2aca490c-aa31-4239-a4cb-608b2eec52e5">

- **Code Snippet:**
  ```python
  Threshhold = 0.8 * 800
  best_math_schools = schools.loc[schools['average_math'] >= Threshhold, ['school_name', 'average_math']]
  best_math_schools = best_math_schools.sort_values(by='average_math', ascending=True)
  print(best_math_schools.head(10))
  ```


### 2. Identifying Top 10 Performing Schools Across All Sections

- **Objective:** Identify the top 10 performing schools based on scores across the three SAT sections, storing the results in a pandas DataFrame named "top_10_schools".

- **Code Snippet:**
  ```python
  # mean(): calculates the average total SAT score per school.
  schools["total_SAT"] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
  top_10_schools = schools.groupby("school_name")["total_SAT"].mean().reset_index().sort_values("total_SAT", ascending=True).head(10)
  fig = plt.figure(figsize=(10,6))
  plt.barh(y=top_10_schools['school_name'], width=top_10_schools['total_SAT'])
  plt.xlabel('SAT SCORES')
  plt.title("Top 10 Performing Schools Across All Sections")
  plt.yticks(fontsize=10)
  plt.show()
  ```

### Top 10 Performing Schools Across All Sections Bar Chart:
<img width="999" alt="Screenshot 2024-01-24 at 2 06 50 AM" src="https://github.com/Gregory204/NYC-SAT-Insights/assets/131078905/0f6d8177-3d29-4faa-a3ae-84860df826e1">


###  Top 10 Performing Schools Across All Sections Table:



### 3. Locating NYC Borough with Largest Standard Deviation

- **Objective:** Locate the NYC borough with the largest standard deviation for "total_SAT" and store the results in a DataFrame named "largest_std_dev". The DataFrame includes the "borough" as the index, "num_schools" for the number of schools in the borough, "average_SAT" for the mean of "total_SAT", and "std_SAT" for the standard deviation.

- **Code Snippet:**
  ```python
  boroughs = schools.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std']).round(2)
  
  largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]
  largest_std_dev = largest_std_dev.rename(columns={'count' : 'num_schools', 'mean' : 'average_SAT', 'std' : 'std_SAT'})
  ```

## Conclusion

The analysis of NYC public school SAT performance provides valuable insights into top-performing schools, specifically in math, across all sections, and identifies the borough with the highest variability in SAT scores. These findings contribute to informed decision-making for education professionals, policymakers, researchers, and parents.
