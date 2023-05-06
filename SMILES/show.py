import openpyxl

# Load the workbook
workbook = openpyxl.load_workbook('example.xlsx')

# Select the sheet you want to work with
worksheet = workbook['Sheet1']

# Specify the column you want to delete empty rows from
column_to_check = 'A'

# Keep track of the non-empty rows in the specified column
non_empty_rows = []

# Loop through all rows in the worksheet
for row in worksheet.iter_rows(min_row=1, max_col=1, values_only=True):
    # If the cell in the specified column is not empty, add the row to the non-empty rows list
    if row[0]:
        non_empty_rows.append(row)

# Get the value of the first row in the specified column
column_label = worksheet[column_to_check + '1'].value

# Create a new worksheet to store the cleaned up version of the data
cleaned_worksheet = workbook.create_sheet(column_label)

# Copy the column label to the new worksheet
cleaned_worksheet.append([column_label])

# Write the non-empty rows to the new worksheet
for row in non_empty_rows:
    cleaned_worksheet.append(row)

# Save the cleaned up version of the workbook to the new sheet
workbook.save('example_cleaned.xlsx')
