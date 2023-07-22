import pandas as pd

# Read the Excel files
file_one = pd.read_excel('file_one.xlsx')
file_two = pd.read_excel('file_two.xlsx')
# Concatenate the two files
concatenated_file = pd.concat([file_one, file_two])

# Save the concatenated file
concatenated_file.to_excel('concatenated_file.xlsx', index=False)