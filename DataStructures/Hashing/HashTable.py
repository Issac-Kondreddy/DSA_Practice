class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return sum(ord(char) for char in key) % self.size

    def set(self, key, value):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Add new key-value pair

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return None  # Key not found

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True  # Key removed
        return False  # Key not found



# Instantiate the HashTable
ht = HashTable()

# Add some key-value pairs
ht.set("name", "Issac")
ht.set("location", "Central Park")
ht.set("language", "Python")

# Retrieve a value
print(ht.get("name"))        # Should print 'Issac'
print(ht.get("location"))    # Should print 'Central Park'

# Attempt to retrieve a non-existent key
print(ht.get("age"))         # Should print 'None'

# Remove a key-value pair
print(ht.remove("language"))  # Should print 'True' indicating successful removal

# Attempt to remove a non-existent key
print(ht.remove("birthday"))  # Should print 'False'

# Attempt to retrieve a removed key
print(ht.get("language"))    # Should print 'None' as it's been removed
