import os
import pandas as pd

current_directory = os.path.dirname(os.path.abspath(__file__))

for filename in os.listdir(current_directory):
    if filename.endswith(".xls") or filename.endswith(".xlsx"):
        file_path = os.path.join(current_directory, filename)
        
        try:
            if filename.endswith(".xls"):
                with open(file_path, 'rb') as f:
                    if f.read(4) == b'<htm':
                        xls_data = pd.read_html(file_path)[0]
                    else:
                        xls_data = pd.read_excel(file_path, engine='xlrd')
            else:
                xls_data = pd.read_excel(file_path, engine='openpyxl')
        except Exception as e:
            print(f"Error {file_path}: {e}")
            continue
        
        csv_filename = filename.replace(".xls", ".csv").replace(".xlsx", ".csv")
        csv_file_path = os.path.join(current_directory, csv_filename)
        
        xls_data.to_csv(csv_file_path, index=False, encoding='utf-8-sig')


print(f"{len([f for f in os.listdir(current_directory) if f.endswith('.csv')])} 파일 완료.")