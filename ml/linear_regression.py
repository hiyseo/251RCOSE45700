import numpy as np

# 데이터 생성
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])  # 정답은 y = 2x

# 파라미터 초기화
w = 0.0
b = 0.0
lr = 0.01

# 경사하강법
for epoch in range(1000):
    y_pred = w * x + b
    error = y_pred - y
    w_grad = (2 / len(x)) * np.dot(error, x)
    b_grad = (2 / len(x)) * np.sum(error)
    w -= lr * w_grad
    b -= lr * b_grad

print(f"최종 결과: w = {w:.4f}, b = {b:.4f}")