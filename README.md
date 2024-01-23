# NYC Public School SAT Performance Analysis

## Overview

This project focuses on analyzing the SAT performance of New York City (NYC) public schools, utilizing the dataset "schools.csv". The SATs, a crucial component of the American high school experience, assess literacy, numeracy, and writing skills. The analysis aims to provide insights into school performance, assisting various stakeholders such as policy and education professionals, researchers, government bodies, and parents making informed decisions about their children's education.

## Key Questions

### 1. Identifying Top Math-Performing Schools

- **Objective:** Create a pandas DataFrame named "best_math_schools" containing the "school_name" and "average_math" score for schools where the math results are at least 80% of the maximum possible score.
  
- **Code Snippet:**
  ```python
  import pandas as pd
  
  schools = pd.read_csv("schools.csv")
  
  Threshold = 0.8 * 800
  best_math_schools = schools.loc[schools['average_math'] >= Threshold, ['school_name', 'average_math']]
  best_math_schools = best_math_schools.sort_values(by='average_math', ascending=False)
  ```

### 2. Identifying Top 10 Performing Schools Across All Sections

- **Objective:** Identify the top 10 performing schools based on scores across the three SAT sections, storing the results in a pandas DataFrame named "top_10_schools".

- **Code Snippet:**
  ```python
  schools["total_SAT"] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
  
  top_10_schools = schools.groupby("school_name")["total_SAT"].mean().reset_index().sort_values("total_SAT", ascending=False).head(10)
  ```

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
