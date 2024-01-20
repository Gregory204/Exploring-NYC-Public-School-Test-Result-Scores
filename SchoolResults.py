import pandas as pd  # import pandas for reading in the data

schools = pd.read_csv("schools.csv")  # this line reads in the data

Threshhold = 0.8 * 800  # Threshhold is used to get at least 80% of the max possible score. (Max score = 800)
best_math_schools = schools.loc[schools['average_math'] >= Threshhold, ['school_name', 'average_math']]  # getting all math scores that are greater than or equal to threshhold
best_math_schools = best_math_schools.sort_values(by='average_math', ascending=False)  # sorting in descending order
'''
Output:
                                           school_name  average_math
88                              Stuyvesant High School           754
170                       Bronx High School of Science           714
93                 Staten Island Technical High School           711
365  Queens High School for the Sciences at York Co...           701
68   High School for Mathematics, Science, and Engi...           683
280                     Brooklyn Technical High School           682
333                        Townsend Harris High School           680
174  High School of American Studies at Lehman College           669
0    New Explorations into Science, Technology and ...           657
45                       Eleanor Roosevelt High School           641
'''

# Getting the total SAT scores and finding the top 10 schools by total scores.
schools["total_SAT"] = schools['average_math'] + schools['average_reading'] + schools['average_writing']  # create column 'total_SAT'
top_10_schools = schools.groupby("school_name")["total_SAT"].mean().reset_index().sort_values("total_SAT", ascending=False).head(10)
# Retrieve the mean() of the schools total score and reset index for index fix and print the top 10 in descending order.
'''
                                           school_name  total_SAT
325                             Stuyvesant High School     2144.0
324                Staten Island Technical High School     2041.0
55                        Bronx High School of Science     2041.0
188  High School of American Studies at Lehman College     2013.0
334                        Townsend Harris High School     1981.0
293  Queens High School for the Sciences at York Co...     1947.0
30                      Bard High School Early College     1914.0
83                      Brooklyn Technical High School     1896.0
121                      Eleanor Roosevelt High School     1889.0
180  High School for Mathematics, Science, and Engi...     1889.0
'''

# Find the NYC borough with the largest standard deviation for 'total_SAT' score
boroughs = schools.groupby('borough')['total_SAT'].agg(['count', 'mean', 'std']).round(2)  # count for each borough, mean total score, and std total score
# .agg(['count', 'mean', 'std']) function
'''
               count     mean     std
borough                              
Bronx             98  1202.72  150.39
Brooklyn         109  1230.26  154.87
Manhattan         89  1340.13  230.29
Queens            69  1345.48  195.25
Staten Island     10  1439.00  222.30
'''

largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]  # gives us borough with the largest std
largest_std_dev = largest_std_dev.rename(columns={'count' : 'num_schools', 'mean' : 'average_SAT', 'std' : 'std_SAT'})  # renaming columns
'''
           num_schools  average_SAT  std_SAT
borough                                     
Manhattan           89      1340.13   230.29
'''
