from __future__ import annotations

from typing import List, Optional


class Heap:
    def __init__(self, data: Optional[List[float]] = None) -> None:
        self.heap = [0.0]  # Используем 0.0 как фиктивный элемент вместо '#'
        if data is not None:
            for el in data:
                self.add(el)

    def add(self, elem: float) -> None:
        self.heap.append(elem)
        i = len(self.heap) - 1
        while i > 1 and self.heap[i] > self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def get_max(self) -> float:
        if len(self.heap) <= 1:
            raise IndexError("Heap is empty")
        return self.heap[1]

    def pop(self) -> float:
        if len(self.heap) == 1:
            raise IndexError("Heap is empty")
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.sift_down(1, len(self.heap))
        return res

    def sift_down(self, i: int, size: int) -> None:
        while 2 * i < size:
            max_idx = 2 * i
            if 2 * i + 1 < size and self.heap[2 * i + 1] > self.heap[max_idx]:
                max_idx = 2 * i + 1

            if self.heap[i] >= self.heap[max_idx]:
                break

            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            i = max_idx

    @staticmethod
    def sort(data: List[float]) -> List[float]:
        if not data:
            return []

        # Создаем кучу с фиктивным элементом
        heap = Heap()
        heap.heap = [0.0] + data.copy()
        n = len(data)

        # Построение кучи
        for i in range(n // 2, 0, -1):
            heap.sift_down(i, n + 1)  # n+1 потому что у нас есть фиктивный элемент

        # Сортировка
        for i in range(n, 1, -1):
            heap.heap[1], heap.heap[i] = heap.heap[i], heap.heap[1]
            heap.sift_down(1, i)

        return heap.heap[1:]  # Исключаем фиктивный элемент

    def __str__(self) -> str:
        if len(self.heap) <= 1:
            return "Empty heap"

        s = []
        level = 0
        while (1 << level) < len(self.heap):
            start = 1 << level
            end = 1 << (level + 1)
            level_nodes = [str(self.heap[i]) for i in range(start, min(end, len(self.heap)))]
            s.append(" ".join(level_nodes))
            level += 1
        return "\n".join(s)

    def str_list(self) -> str:
        return str(self.heap[1:])  # Исключаем фиктивный элемент
