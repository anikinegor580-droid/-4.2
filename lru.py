class _Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self._capacity = capacity
        self._head = _Node()
        self._tail = _Node()
        self._head.next = self._tail
        self._tail.prev = self._head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node):
        prev_node = self._tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self._tail
        self._tail.prev = node

    def _move_to_tail(self, node):
        self._remove(node)
        self._add_to_tail(node)

    def get(self, key):
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._move_to_tail(node)
        return node.value

    def put(self, key, value):
        if self._capacity <= 0:
            return

        if key in self._cache:
            node = self._cache[key]
            node.value = value
            self._move_to_tail(node)
            return

        if len(self._cache) >= self._capacity:
            oldest = self._head.next
            self._remove(oldest)
            del self._cache[oldest.key]

        new_node = _Node(key, value)
        self._cache[key] = new_node
        self._add_to_tail(new_node)
