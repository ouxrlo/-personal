# 필요한 라이브러리 불러오기
import pandas as pd
import numpy as np
import seaborn as sns                # 고급 시각화 기능 라이브러리
import matplotlib.pyplot as plt       # 그래프 표시 및 화면 출력하는 기본적인 시각화 라이브러리

# 파일 경로 지정 및 데이터프레임 불러오기
file_path = '/Users/t2023-m0093/Desktop/개인 과제/housingdata.csv'
df = pd.read_csv(file_path)

# 데이터프레임 정보 확인
df.info()

# 결측치 확인
print(df.isnull().sum())  # 각 열에 있는 결측치의 수 출력