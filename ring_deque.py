class Deque:
    def __init__(self):
        self._capacity = 4
        self._size = 0
        self._head = 0
        self._data = [None] * self._capacity

    @property
    def capacity(self):
        return self._capacity

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[(self._head + i) % self._capacity]
        self._data = new_data
        self._capacity = new_capacity
        self._head = 0

    def push_back(self, item):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        tail_idx = (self._head + self._size) % self._capacity
        self._data[tail_idx] = item
        self._size += 1

    def push_front(self, item):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._head = (self._head - 1) % self._capacity
        self._data[self._head] = item
        self._size += 1

    def pop_back(self):
        if self.is_empty():
            raise IndexError("pop from empty deque")
        tail_idx = (self._head + self._size - 1) % self._capacity
        value = self._data[tail_idx]
        self._data[tail_idx] = None
        self._size -= 1
        return value

    def pop_front(self):
        if self.is_empty():
            raise IndexError("pop from empty deque")
        value = self._data[self._head]
        self._data[self._head] = None
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return value

    def back(self):
        if self.is_empty():
            raise IndexError("back from empty deque")
        tail_idx = (self._head + self._size - 1) % self._capacity
        return self._data[tail_idx]

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty deque")
        return self._data[self._head]
