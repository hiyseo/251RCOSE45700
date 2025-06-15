import numpy as np

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0, 0, 0, 1])  # AND gate

w = np.zeros(X.shape[1])
b = 0
lr = 0.1

for epoch in range(10):
    for i in range(len(X)):
        z = np.dot(X[i], w) + b
        pred = 1 if z > 0 else 0
        error = y[i] - pred
        w += lr * error * X[i]
        b += lr * error

print("학습된 가중치:", w)
print("학습된 바이어스:", b)
print("예측 결과:", [1 if np.dot(x, w)+b > 0 else 0 for x in X])