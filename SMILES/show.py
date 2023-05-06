import openpyxl

# Load the Excel workbook
workbook = openpyxl.load_workbook('my_workbook.xlsx')

# Select a specific sheet by name
worksheet = workbook['Sheet1']

# Set the column number you want to remove empty rows from
column_number = 1

# Loop through all the rows in the sheet
for row in worksheet.iter_rows():
    # Check if the cell in the specified column is empty
    if not row[column_number-1].value:
        # If it is empty, delete the row
        worksheet.delete_rows(row[0].row)

# Save the workbook with the changes
workbook.save('my_workbook.xlsx')
