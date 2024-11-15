import pandas as pd

def main():
    y_m = file.split("_")[1].split(".")[0]
    y_m = y_m.split("년")
    y_m = y_m[0] + "-" + y_m[1]
    y_m = y_m.replace("월", "-")
    print(y_m)

    file_path = '일산화탄소/'+file
    data = pd.read_csv(file_path)

    data.columns = data.iloc[0] 
    data = data.drop(0).reset_index(drop=True)  #헤더 행 제거
    data = data.rename(columns={"시군": "지역", "측정소": "측정소명"})  #열 이름 변경

    data = data[data["지역"] != "통합"].reset_index(drop=True)
    data_long = pd.melt(data, id_vars=["지역", "측정소명"], var_name="날짜", value_name="일산화탄소 농도")
    data_long["날짜"] = y_m + data_long["날짜"].str.replace("일", "").str.zfill(2)

    data_long["일산화탄소 농도"] = data_long["일산화탄소 농도"].replace("-", 0).fillna(0)

    data_long = data_long.reset_index(drop=True)

    output_file_path = "n_"+file
    data_long.to_csv(output_file_path, index=False, encoding='utf-8-sig')  # 인코딩 설정 추가

    print(data_long)

for i in range(1, 13):
    if len(str(i)) == 1:
        i="0"+str(i)
    file = f'기간별_2017년{i}월.csv'
    y_m = file.split("_")[1].split(".")[0]
    y_m = y_m.split("년")
    y_m = y_m[0] + "-" + y_m[1]
    y_m = y_m.replace("월", "-")
    print(y_m)
    main()

# file_path = '미세먼지 데이터_강원전체/'+file
# data = pd.read_csv(file_path)

# data.columns = data.iloc[0] 
# data = data.drop(0).reset_index(drop=True)  #헤더 행 제거
# data = data.rename(columns={"시군": "지역", "측정소": "측정소명"})  #열 이름 변경

# data = data[data["지역"] != "통합"].reset_index(drop=True)
# data_long = pd.melt(data, id_vars=["지역", "측정소명"], var_name="날짜", value_name="미세먼지 농도")
# data_long["날짜"] = y_m + data_long["날짜"].str.replace("일", "").str.zfill(2)

# data_long["미세먼지 농도"] = data_long["미세먼지 농도"].replace("-", 0).fillna(0)

# data_long = data_long.reset_index(drop=True)

# output_file_path = "n_"+file
# data_long.to_csv(output_file_path, index=False, encoding='utf-8-sig')  # 인코딩 설정 추가

# print(data_long)