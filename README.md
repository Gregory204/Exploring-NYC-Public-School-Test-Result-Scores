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

### Top 10 Performing Schools Across All Sections Horizontal Bar Chart:
<img width="999" alt="Screenshot 2024-01-24 at 2 06 50 AM" src="https://github.com/Gregory204/NYC-SAT-Insights/assets/131078905/0f6d8177-3d29-4faa-a3ae-84860df826e1">


###  Top 10 Performing Schools Across All Sections SQL Table:
<img width="314" alt="Screenshot 2024-01-24 at 9 35 45 AM" src="https://github.com/Gregory204/NYC-SAT-Insights/assets/131078905/f1c82389-9547-49df-b860-8af79e4b2a68">


### 3. Locating NYC Borough with Highest Number of Schools, Largest mean for SAT scores, and Largest Standard Deviation:

- **First Objective:** Locating NYC Borough with Highest Number of Schools. Store it in a variable called largest_count that gives us the borough with the highest quanity of schools in that borough. 

- **Code Snippet:**
  ```python
  schools["total_SAT"] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
  boroughs = schools.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std']).round(2)
  boroughs = boroughs.rename(columns={'count' : 'num_schools', 'mean' : 'average_SAT', 'std' : 'std_SAT'})
  largest_count = boroughs[boroughs['num_schools'] == boroughs['num_schools'].max()]
  largest_mean = boroughs[boroughs['average_SAT'] == boroughs['average_SAT'].max()]
  largest_std_dev = boroughs[boroughs['std_SAT'] == boroughs['std_SAT'].max()]
  
  bor_label = []
  for c in schools['borough'].unique():
    bor_label.append(c)

  colors = ['skyblue', 'orange', 'blue', 'green', 'yellow']
  fig, ax = plt.subplots(figsize=(10, 6))

  for borough, color in zip(boroughs.index, colors):
    ax.barh(width=boroughs.loc[borough, 'num_schools'], y=borough, color=color, label=f'{borough}')

  ax.set_xlabel('School Count')
  ax.set_title('Number Of Schools in Each Borough')
  ax.legend()
  plt.show()
  ```
### Locating NYC Borough with Highest Number of Schools Bar Chart:
<img width="995" alt="Screenshot 2024-01-24 at 2 47 49 PM" src="https://github.com/Gregory204/NYC-SAT-Insights/assets/131078905/651ccb53-4e52-41a2-8d60-41107ac2ed8d">

By this image we can say out of the 5 boroughs Brooklyn offers more schools than the other two. Thus granting kids multiple locations for an education if they live in the borough Brooklyn.

- **Second Objective:** Locating NYC Borough with the largest mean for SAT scores. Store it in a variable called largest_mean that gives us the borough with the largest SAT score of schools in that borough. 

- **Code Snippet:**
  ```python
  for borough, color in zip(boroughs.index, colors):
    ax.barh(width=boroughs.loc[borough, 'std_SAT'], y=borough, color=color, label=f'{borough}')

  ax.set_xlabel('SAT Scores')
  ax.set_title('SAT Scores Across Boroughs')
  ax.legend()
  plt.show()
  ```

### Locating NYC Borough with Largest SAT Score Bar Chart:
<img width="997" alt="Screenshot 2024-01-24 at 2 52 44 PM" src="https://github.com/Gregory204/NYC-SAT-Insights/assets/131078905/266de7d4-f5f4-4d11-ac70-16f170160c36">

This chart shows us that in the borough of Staten Island, Kids are flourishing on the SAT. Giving parents insights that schools in Staten Island can help their kids with getting high academic achievements in the future if they sent their kids to a school in this borough.

**Third Objective:** Locating NYC Borough with the largest standard deviations. Store it in a variable called largest_mean that gives us the borough with the largest SAT score of schools in that borough. 

### Locating NYC Borough with Largest Standard Deviation Value Bar Chart:
<img width="1000" alt="Screenshot 2024-01-24 at 2 57 17 PM" src="https://github.com/Gregory204/NYC-SAT-Insights/assets/131078905/8f462234-40df-473a-a57e-7ead8af9c29b">

This chart shows us that in the borough of Manhattan there is a lot of educational diversity. However, a high standard deviation can indicate that the some schools are acheiving high scores while others aren't acheiving as high as the well performimg schools. It's a lot to consider.

## Conclusion

The analysis of NYC public school SAT performance provides valuable insights into top-performing schools, specifically in math, across all sections, and identifies the borough with the highest variability in SAT scores. These findings contribute to informed decision-making for education professionals, policymakers, researchers, and parents.
