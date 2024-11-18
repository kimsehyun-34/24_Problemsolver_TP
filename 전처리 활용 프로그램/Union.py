import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))

csv_files = [f for f in os.listdir(current_dir) if f.endswith('.csv')]
df_list = []
for file in csv_files:
    try:
        df_list.append(pd.read_csv(os.path.join(current_dir, file), encoding='utf-8'))
    except pd.errors.EmptyDataError:
        print(f"Empty data file skipped: {file}")

if df_list:
    combined_df = pd.concat(df_list, ignore_index=True)
    combined_df.to_csv(os.path.join(current_dir, 'combined.csv'), index=False, encoding='utf-8-sig')
    print("성공")
else:
    print("연결할 데이터프레임이 없습니다.")