import heapq

class Node:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.freq < other.freq


heap = []
freqs = {
    'A': 5,
    'B': 9,
    'C': 12,
    'D': 13,
    'E': 16,
    'F': 45
}
for char, freq in freqs.items():
    heapq.heappush(heap, Node(char, freq))

while len(heap)>1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)
    merged = Node(None, left.freq + right.freq, left, right)
    heapq.heappush(heap, merged)
root = heap[0]


def generate_code(node, current_code = "", codes={}):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
        return
    generate_code(node.left, current_code + "0", codes)
    generate_code(node.right, current_code + "1", codes)
    return codes

def encode(text, codes):
    encoded_text = ""
    for char in text:
        encoded_text += codes[char]
    return encoded_text
def decode(encoded_text, root):
    text = ""
    current = root
    for bit in encoded_text:
        if bit=="0":
            current = current.left
        else:
            current = current.right
        if current.char is not None:
            text += current.char
            current = root
    return text
codes = generate_code(root)
print("Huffman Codes: ")
for char in codes:
    print(f"{char}:{codes[char]}")

text = "FACE"
encoded = encode(text, codes)
print("Encoded:", encoded)

decoded = decode(encoded, root)
print("Decoded:", decoded)
