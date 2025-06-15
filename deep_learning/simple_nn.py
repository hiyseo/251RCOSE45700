import numpy as np
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0]])
def sigmoid(x): return 1 / (1 + np.exp(-x))
def deriv(x): return sigmoid(x)*(1-sigmoid(x))
w1 = 2*np.random.rand(2,4)-1; w2 = 2*np.random.rand(4,1)-1
for _ in range(10000):
    l1 = sigmoid(np.dot(X, w1))
    l2 = sigmoid(np.dot(l1, w2))
    l2_delta = (y - l2) * deriv(l2)
    l1_delta = l2_delta.dot(w2.T) * deriv(l1)
    w2 += l1.T.dot(l2_delta); w1 += X.T.dot(l1_delta)
print("output:", l2)