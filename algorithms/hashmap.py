class HashMap:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.buckets[index]

        print(key, value)
        for i, (k, v) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))


hashmap = HashMap()
hashmap.put("hammes", 3)
hashmap.put("hammes", 5)
print(hashmap.buckets)

#get
#delete
#resizing
#linked-list
#doc