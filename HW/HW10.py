import numpy as np

def n_dimensional_integral(func, lower_bounds, upper_bounds, num_samples=1000000):
    """
    使用蒙地卡羅法計算 n 維積分
    :param func: 待積分函數 (接受一個長度為 n 的 array)
    :param lower_bounds: 各維度下限 (list 或 array)
    :param upper_bounds: 各維度上限 (list 或 array)
    :param num_samples: 採樣點數量
    :return: 積分估計值
    """
    # 確保輸入為 numpy 陣列
    low = np.array(lower_bounds)
    high = np.array(upper_bounds)
    dims = len(low)
    
    # 1. 在 n 維長方體區域內產生隨機採樣點
    # 產生的矩陣形狀為 (num_samples, dims)
    pts = np.random.uniform(low, high, (num_samples, dims))
    
    # 2. 計算所有點的函數值
    # 使用 np.apply_along_axis 處理自定義函數
    f_values = np.apply_along_axis(func, 1, pts)
    
    # 3. 計算積分區域的體積 (所有維度差的乘積)
    volume = np.prod(high - low)
    
    # 4. 積分值 = 體積 * 函數平均值
    integral = volume * np.mean(f_values)
    
    return integral

# --- 測試範例 ---
# 假設我們要積分 f(x, y, z) = x + y^2 + sin(z)
# 範圍：x:[0,1], y:[0,1], z:[0, pi]
def test_func(args):
    x, y, z = args
    return x + y**2 + np.sin(z)

if __name__ == "__main__":
    low_b = [0, 0, 0]
    high_b = [1, 1, np.pi]
    
    result = n_dimensional_integral(test_func, low_b, high_b)
    print(f"3維積分測試結果: {result:.6f}")
    # 理論值計算：
    # ∫(0->1) x dx = 0.5
    # ∫(0->1) y^2 dy = 1/3 ≈ 0.3333
    # ∫(0->pi) sin(z) dz = 2
    # 總和：(0.5 + 0.3333 + 2) * (1*1*pi) / (1*1*pi) = 2.8333...
