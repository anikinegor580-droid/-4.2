class DynamicArray:
    def __init__(self):
        self._capacity = 4
        self._size = 0
        self._data = [None] * self._capacity

    @property
    def capacity(self):
        return self._capacity

    def __len__(self):
        return self._size

    def _check_index(self, index):
        if not (0 <= index < self._size):
            raise IndexError("index out of range")

    def __getitem__(self, index):
        self._check_index(index)
        return self._data[index]

    def __setitem__(self, index, value):
        self._check_index(index)
        self._data[index] = value

    def _resize(self, new_capacity):
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def append(self, item):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = item
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty dynamic array")
        value = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return value
