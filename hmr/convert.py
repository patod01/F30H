import datetime
from decimal import Decimal
import csv

# this is for a specific data

def convert_input_format(input_str):
   parsed_tuple = eval(input_str)
   username = parsed_tuple[0]
   email = parsed_tuple[1]
   date = parsed_tuple[2]
   decimal_value = parsed_tuple[3]
   last_number = parsed_tuple[4]
   return [
       username,
       email,
       f'{date.year}-{date.month:02}-{date.day:02}',
       float(decimal_value),
       last_number
    ]

# Read input from txt file
with open('hh_py.csv', 'r') as input_file:
   input_lines = input_file.readlines()

# Process and write to CSV
with open('output.csv', 'w', newline='') as output_file:
   csv_writer = csv.writer(output_file)

   for line in input_lines:
        converted_line = convert_input_format(line)
        csv_writer.writerow(converted_line)

print('Conversion complete. Check output.csv')
