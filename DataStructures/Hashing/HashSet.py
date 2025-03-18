class HashSet:
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

    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.array[index]
        if value in bucket:
            val = bucket.remove(value)
            return f"{val} removed"
        return f"{value} not found"


# Example usage
ht = HashSet()
ht.add("Issac")
ht.add("Pranay")
ht.add("bharadwaj")
print(ht.contains("Pranay"))
print(ht.contains("someone else"))
ht.remove("Pranay")
print(ht.contains("Pranay"))