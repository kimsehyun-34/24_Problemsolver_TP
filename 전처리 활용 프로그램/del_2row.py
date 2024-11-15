import os
import csv

current_directory = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(current_directory):
    if filename.endswith('.csv'):
        file_path = os.path.join(current_directory, filename)
        
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = list(csv.reader(csvfile))
        
        if len(reader) > 1:
            del reader[1]
        
        # Delete 'C' column (index 2)
        for row in reader:
            if len(row) > 2:
                del row[2]
        
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(reader)