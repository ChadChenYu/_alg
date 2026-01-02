import numpy as np

# 1. 準備數據 (y = 2x + 1)
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

def get_loss(w, b, x, y):
    predict = w * x + b
    return np.mean((y - predict) ** 2)

# --- 1. 爬山算法 (Hill Climbing) ---
def hill_climbing(x, y, iterations=1000, step=0.01):
    w, b = 0.0, 0.0
    current_loss = get_loss(w, b, x, y)
    
    for _ in range(iterations):
        # 隨機嘗試微調 w 或 b
        dw = np.random.uniform(-step, step)
        db = np.random.uniform(-step, step)
        
        next_loss = get_loss(w + dw, b + db, x, y)
        if next_loss < current_loss:
            w, b = w + dw, b + db
            current_loss = next_loss
            
    return w, b, current_loss

# --- 2. 貪婪法 (Greedy Method) ---
# 在每個維度（w, b）選擇當下最優的方向
def greedy_method(x, y, iterations=1000, step=0.01):
    w, b = 0.0, 0.0
    
    for _ in range(iterations):
        # 測試 w 的三種可能：增加、減少、不變
        best_w, best_b = w, b
        min_loss = get_loss(w, b, x, y)
        
        for dw in [-step, 0, step]:
            for db in [-step, 0, step]:
                loss = get_loss(w + dw, b + db, x, y)
                if loss < min_loss:
                    min_loss = loss
                    best_w, best_b = w + dw, b + db
        w, b = best_w, best_b
        
    return w, b, get_loss(w, b, x, y)

# --- 3. 陡峭下降法 (Steepest Descent / Gradient Descent) ---
def steepest_descent(x, y, iterations=1000, learning_rate=0.01):
    w, b = 0.0, 0.0
    n = len(x)
    
    for _ in range(iterations):
        y_pred = w * x + b
        # 計算梯度
        dw = (-2/n) * np.sum(x * (y - y_pred))
        db = (-2/n) * np.sum(y - y_pred)
        
        # 更新參數
        w -= learning_rate * dw
        b -= learning_rate * db
        
    return w, b, get_loss(w, b, x, y)

# 測試結果
print(f"爬山算法: {hill_climbing(x, y)}")
print(f"貪婪法: {greedy_method(x, y)}")
print(f"陡峭下降法: {steepest_descent(x, y)}")
