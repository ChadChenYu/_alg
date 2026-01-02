(A-Star) 搜尋演算法
演算法筆記：A*搜尋演算法 (A-Star Search)1. 什麼是 A*？
A* 是一種啟發式（Heuristic）搜尋演算法，用於在圖形（Graph）或網格中尋找從起點到終點的最短路徑。
它結合了 Dijkstra 演算法（保證最短路徑）與 最佳優先搜尋 (BFS)（效率高）的優點。
核心公式A* 的精髓在於它的估值函數：f(n) = g(n) + h(n)：節點 n 的總估計代價。
g(n)：從起點到當前節點 n 的實際移動代價。
h(n)：從節點 n 到終點的預計代價（啟發式函數）。
這通常使用曼哈頓距離（Manhattan Distance）或歐幾里得距離來計算。
程式碼:
import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # 到起點的距離
        self.h = 0  # 到終點的預計距離
        self.f = 0  # 總代價

    def __lt__(self, other):
        return self.f < other.f

def astar(maze, start, end):
    # 初始化起點與終點節點
    start_node = Node(start)
    end_node = Node(end)

    # 待探索清單 (Open List) 與 已探索清單 (Closed List)
    open_list = []
    closed_set = set()

    # 將起點加入 Open List
    heapq.heappush(open_list, start_node)

    while open_list:
        # 取得 f 值最小的節點
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)

        # 檢查是否到達終點
        if current_node.position == end_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1] # 回傳反轉後的路徑

        # 產生鄰居節點 (上下左右)
        (x, y) = current_node.position
        for next_pos in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            
            # 檢查邊界與障礙物
            if (0 <= next_pos[0] < len(maze)) and (0 <= next_pos[1] < len(maze[0])):
                if maze[next_pos[0]][next_pos[1]] == 1: continue
                if next_pos in closed_set: continue

                neighbor = Node(next_pos, current_node)
                neighbor.g = current_node.g + 1
                # 啟發式函數：曼哈頓距離
                neighbor.h = abs(neighbor.position[0] - end_node.position[0]) + \
                             abs(neighbor.position[1] - end_node.position[1])
                neighbor.f = neighbor.g + neighbor.h

                # 如果鄰居不在 open_list 中，或有更短的 g 值，則加入/更新
                heapq.heappush(open_list, neighbor)

    return None

# --- 測試資料 ---
grid = [
    [0, 0, 0, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]
start_pos = (0, 0)
end_pos = (4, 4)

path = astar(grid, start_pos, end_pos)
print(f"從 {start_pos} 到 {end_pos} 的最短路徑為：\n{path}")


使用Gemini生成:https://gemini.google.com/share/c56c41583534
