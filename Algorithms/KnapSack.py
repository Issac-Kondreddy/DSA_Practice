class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
def KnapSack(items:list[Item], index:int, capacity:int):
    if index<0 or capacity ==0:
        return 0
    item = items[index]
    if item.weight > capacity:
        return KnapSack(items, index-1, capacity)
    include = item.value  + KnapSack(items, index-1, capacity - item.weight)
    exclude = KnapSack(items, index-1, capacity)
    return max(include, exclude)


items = [Item(1, 1), Item(3, 4), Item(4, 5), Item(5, 7)]
W = 7
result = KnapSack(items, len(items) - 1, W)
print(result)

