import pandas as pd
import glob
import os

# Path to the directory containing CSV files to be combined
pathToCsv = os.getcwd()+"/dropCsvHere/"

# Use glob to get a list of all CSV files in the directory
csv_files = glob.glob(pathToCsv + '*.csv')

# Create an empty list to hold the dataframes
dfs = []

# Loop through each CSV file and read it into a dataframe
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    dfs.append(df)

# Concatenate all dataframes into one
combined_df = pd.concat(dfs, ignore_index=True)

# Write the combined dataframe to a new CSV file
combined_df.to_csv('combined.csv', index=False)
