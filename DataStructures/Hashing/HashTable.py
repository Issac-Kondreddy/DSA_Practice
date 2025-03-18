class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.array = [[] for _ in range(self.size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        index = self.hash_function(value)
        bucket = self.array[index]
        if value not in bucket:
            bucket.append(value)

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.array[index]
        return value in bucket

# Example usage
ht = HashTable()
ht.add("Issac")
ht.add("Pranay")
ht.add("bharadwaj")
print(ht.contains("Pranay"))
print(ht.contains("someone else"))
