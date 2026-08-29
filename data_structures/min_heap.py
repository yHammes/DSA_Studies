class MinHeap:
    def __init__(self):
        self.heap = []

    def _left_child(selfself, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _heapify_up(self, index):
        if index == 0:
            return

        paratent_index = self._parent(index)
        if self.heap[index] < self.heap[paratent_index]:
            self.heap[index], self.heap[paratent_index] = self.heap[paratent_index], self.heap[index]

            self._heapify_up(paratent_index)

    def _heapify_down(self, index):
        left = self._left_child(index)
        right = self._right_child(index)

        smallest = index

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def pop_min(self) :
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root



min_heap = MinHeap()
min_heap.insert(3)
min_heap.insert(4)
min_heap.insert(1)