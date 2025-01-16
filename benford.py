import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib

# 한글 폰트 설정
matplotlib.rcParams['font.family'] = 'AppleGothic'  # 맥북에서 기본적으로 제공되는 한글 폰트
matplotlib.rcParams['axes.unicode_minus'] = False   # 마이너스 기호 처리

# 100만 개의 지수 분포를 따르는 숫자 생성
data = np.random.exponential(scale=1000, size=1000000).astype(int)

# 첫 번째 자릿수 추출 함수
def first_digit(num):
    while num >= 10:
        num //= 10
    return num

# 첫 번째 자릿수 리스트 만들기
first_digits = [first_digit(num) for num in data]

# 1부터 9까지
counts = {i: first_digits.count(i) for i in range(1, 10)}

# 벤포드의 법칙 이론적 확률 계산
benford_probs = [math.log10(1 + 1/d) for d in range(1, 10)]

# 실제 데이터
total = sum(counts.values())
actual_probs = [counts[d] / total * 100 for d in range(1, 10)]

# 벤포드의 법칙에 따른 예상 비율을 100으로 맞춤
benford_probs_percent = [p * 100 for p in benford_probs]

# 그래프 그리기
plt.figure(figsize=(10, 6))

#막대그래프
plt.bar(counts.keys(), actual_probs, label="실제 데이터", alpha=0.6)

#선 그래프
plt.plot(range(1, 10), benford_probs_percent, label="벤포드의 법칙", color='red', marker='o')

plt.title('벤포드의 법칙 테스트')
plt.xlabel('첫 번째 자릿수')
plt.ylabel('비율 (%)')
plt.xticks(range(1, 10))
plt.legend()
plt.grid(True)
plt.show()

