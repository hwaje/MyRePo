# 2단부터 9단까지 구구단 출력
for i in range(2, 10):  # 2부터 9까지 반복
    print(f"--- {i}단 ---")
    for j in range(1, 10):  # 1부터 9까지 곱함
        print(f"{i} x {j} = {i * j}")
    print()  # 각 단 사이에 빈 줄 추가