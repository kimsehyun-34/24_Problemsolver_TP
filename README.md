# 24_Problemsolver_TP
------
<div>
  <img style="float:left" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&amp;logo=python&amp;logoColor=white" width="auto" height="40" />
  <img style="float:left" src="https://img.shields.io/badge/Google Colab-F9AB00?style=flat-square&amp;logo=google colab&amp;logoColor=white" width="auto" height="40" />
  <img style="float:left" src="https://img.shields.io/badge/Excel-217346?style=flat-square&amp;logo=microsoft excel&amp;logoColor=white" width="auto" height="40" />
</div>
------

# 전처리 활용 프로그램
- `Union.py` ---> 같은 칼럼을 가진 데이터 파일들을 하나의 파일로 합치는데 사용. (폴더에 csv파일들과 Union.py를 넣고 실행)
- `XLStoCSV.py` ----> XLS파일을 CSV파일로 변환하는데사용
- `del_2row.py` ----> 전처리 작업중 2번째 칼럼을 제거할때 사용
- `pivot.py` ----> 칼럼이 1일, 2일 , ... , 30일 이렇게 구성되어 있는 경우 이들을 인덱스 값으로 변환 (Pivot or Unpivot 기능)

`파일마다 호환이 안되는 파일이 있을 수 있습니다.
파이썬 코드를 열어보고 데이터 파일 구성에 맞게 다시 패치해서 사용하시면 될 거 같습니다.`

------
## 과제 정보
- 강원도, 수도권 등의 특정 지역을 분석해도 좋고 전체 분석도 좋음
- 분석 및 예측 기간도 팀에서 자체 결정
- 어떤 데이터를 쓰는지도 팀내에서 수집 및 결정
- 단 발표시 위 3가지 내용(지역, 시기, 데이터)을 결정하게 된 이유를 간략하게 설명하기

-----
# 주제 : 강원도 지역의 초미세먼지, 미세먼지 농도 예측
- 종속변수 = 하루 미세먼지 농도 (PM10)
- 독립변수 = 평균기온, 최저기온, 일강수량, 기압, 전날 미세먼지 농도, 이산화탄소 농도, 유해가스 농도, 자동차 보유수 (자동차 유동수, 하루 자동차 통행량), 공장보유수, 평균풍속, 평균전운량, 평균중하층운량, 평균지면온도, 가조시간, 합계일조시간, 지역 평균 배기가스 배출량

-----
## 수집 조건
- 2017년 1월 1일 ~ 2024년 1월 1일 (24년 데이터가 없는 경우 : 23년 12월 31일 데이터로) 까지의 데이터 수집.
- 강원도에 있는 '시' 전체 수집.
- '일' 단위로 해서 수집.
- 각각 4개씩 나눠서 전송.
- 데이터 파일은 .CSV 파일로.
--------
- 호준 - 평균기온, 최저기온, 일강수량, 기압
- 재민 - 전날 미세먼지 농도, 이산화탄소 농도, 유해가스 농도, 지역내 자동차 보유 수
- 세현 - 공장보유수, 평균풍속, 평균전운량, 평균중하층운량, 하루 미세먼지 농도 (PM10)
- 나연 - 평균 지면온도, 평균 일조시간, 하루 구름 량(구름 크기 or 넓이), 지역 평균 배기가스 배출량

-------
## 자료 수집 페이지
[[붙임2] 데이터 플랫폼 목록.pdf](https://github.com/user-attachments/files/17659276/2.pdf)

----
- [미세먼지 & 오염가스 데이터 % 대기기상 수집 주소](https://www.airgangwon.go.kr/gwair/statistics/period/by_month) - `https://www.airgangwon.go.kr/gwair/statistics/period/by_month`
- [기온 & 지면기상 데이터 수집 주소](https://data.kma.go.kr/climate/RankState/selectRankStatisticsDivisionList.do) - `https://data.kma.go.kr/climate/RankState/selectRankStatisticsDivisionList.do`

