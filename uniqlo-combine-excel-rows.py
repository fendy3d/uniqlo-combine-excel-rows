import pandas as pd
import glob
import os

# Path to the directory containing CSV files to be combined
pathToCsv = os.getcwd()+"/dropCsvHere/"

# user input
userinput_wantSum = input("Do you want to sum a particular column? Press 1 for yes, press anything for no.")

if userinput_wantSum == '1':
    userinput_columnNumber = input("Which column number do you want to sum? If first row, press 1.")



# Use glob to get a list of all CSV files in the directory
csv_files = glob.glob(pathToCsv + '*.csv')

# Create an empty list to hold the dataframes
dfs = []

# Loop through each CSV file and read it into a dataframe
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Calculate the sum
if userinput_wantSum == '1':
    sum_of_column = df.iloc[:, int(userinput_columnNumber)-1].sum()
    print("The sum of column {}: {}".format(userinput_columnNumber, sum_of_column))

# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Write the combined dataframe to a new CSV file
combined_df.to_csv('combined.csv', index=False)

print('combined.csv is created. All hail lord Fendy')