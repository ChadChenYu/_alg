def is_safe(queens, row, col):
    """檢查在 (row, col) 是否可放皇后"""
    for r, c in enumerate(queens):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_queens(n=8):
    queens = []   # queens[row] = col，存每一列皇后的位置

    def dfs(row):
        if row == n:
            print("\n✅ 找到一個解！")
            print_solution(queens)
            return True  # 找到第一個解就停止

        for col in range(n):
            print(f"嘗試在第 {row} 列，第 {col} 行放皇后...")

            if is_safe(queens, row, col):
                print(f"✔ 可以放！放在 ({row}, {col})")
                queens.append(col)

                if dfs(row + 1):  # 繼續到下一列
                    return True

                # 回溯
                print(f"✘ 從 ({row}, {col}) 回溯，移除皇后")
                queens.pop()
            else:
                print(f"✘ 不能放在 ({row}, {col})，衝突")

        return False

    dfs(0)


def print_solution(queens):
    """輸出台盤圖形"""
    n = len(queens)
    for r in range(n):
        row = ["Q" if c == queens[r] else "." for c in range(n)]
        print(" ".join(row))


# 主程式執行
solve_queens(8)
