class HashMap:
    def __init__(self, size=10):
        self._size = size
        self._buckets = [[] for _ in range(size)]
        self._count = 0

    def _bucket_index(self, key):
        return hash(key) % self._size

    def put(self, key, value):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._count += 1

    def get(self, key):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self._count -= 1
                return
        raise KeyError(key)

    def contains(self, key):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for k, _ in bucket:
            if k == key:
                return True
        return False

    def __len__(self):
        return self._count
