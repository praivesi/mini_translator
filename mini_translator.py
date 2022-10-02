import pandas as pd

CSV_파일 = pd.read_csv('C:/Users/User/Desktop/미니_투잡_파이썬/asset/input/매출관리_2022_04_csv.CSV', encoding='euc-kr')

print(CSV_파일.head())