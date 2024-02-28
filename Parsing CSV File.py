import csv
with open("D:/Downloads/annual-enterprise-survey-2021-financial-year-provisional-csv.csv", 'r') as file:
    csv_reader = csv.reader(file)  # Creates a reader to work with the CSV data   for row in csv_reader:
    # Example: To get the value in the first column of each row
    for row in csv_reader:
     first_column_value = row[4] 
     print(first_column_value)