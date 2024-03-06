import openpyxl

# Create a new workbook and select the active sheet
workbook = openpyxl.Workbook()
sheet = workbook.active

# Data to be written
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 22, 'Los Angeles']
]

# Write data to multiple cells using a cell range
cell_range = sheet['A1':'C4']
for row_index, row_data in enumerate(data):
    for col_index, cell_data in enumerate(row_data):
        cell_range[row_index][col_index].value = cell_data

# Save the workbook to a file
workbook.save('example.xlsx')
