class HashMap:
    """
    A simple Hash Map implementation using Separate Chaining.
    """

    def __init__(self, size=10):
        """Initializes the HashMap with a fixed number of buckers"""
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        """Generate an hash index for a given key"""
        return hash(key) % self.size

    def put(self, key, value):
        """Puts a value into the hash map"""
        index = self._hash(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
                return

        bucket.append((key, value))

    def get(self, key):
        """Retrieves the value associated with the key"""
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v

        return False

    def remove(self, key):
        """Removes the value associated with the key"""
        index = self._hash(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return True

        return False

hashmap = HashMap()
hashmap.put("hammes", 3)
hashmap.put("hammes", 5)
print(hashmap.remove("hammes"))
print(hashmap.get("hammes"))

#resizing
#linked-list
#doc