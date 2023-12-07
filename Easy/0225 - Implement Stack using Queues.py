# 両端キューの実装のクラス
from collections import deque

class MyStack:

    def __init__(self):
        # dequeを用いてキューを初期化
        self.queue = deque()

    def push(self, x: int) -> None:
        q = self.queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
