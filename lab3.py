from collections import defaultdict, deque
import time

print("Яцула Артем Романович, 090301-ПОВа-о24")
print("Выводятся первые 10 символов\n")

pairs = [(chr(97 + i), chr(97 + i + 1)) for i in range(1000)]
print("Исходные пары:", pairs[:9], "\n")

print("-" * 30)
print("Метод A: через массивы")
print("-" * 30)

start = time.time()

letters = []
for a, b in pairs:
    if a not in letters:
        letters.append(a)
    if b not in letters:
        letters.append(b)

graph = [[] for _ in letters]
indeg = [0 for _ in letters]

for a, b in pairs:
    i = letters.index(a)
    j = letters.index(b)
    graph[i].append(j)
    indeg[j] += 1

queue = []
for i in range(len(letters)):
    if indeg[i] == 0:
        queue.append(i)

result = []
while queue:
    current = queue.pop(0)
    result.append(current)
    for neigh in graph[current]:
        indeg[neigh] -= 1
        if indeg[neigh] == 0:
            queue.append(neigh)

if len(result) < len(letters):
    print("Противоречие!")
else:
    order = [letters[i] for i in result]
    print("Полный порядок:", order[:10])

end = time.time()
print("Время выполнения метода A:", end - start, "сек\n")

print("-" * 30)
print("Метод Б: через связанный список")
print("-" * 30)

start = time.time()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value

    def is_empty(self):
        return self.head is None

letters = []
for a, b in pairs:
    if a not in letters:
        letters.append(a)
    if b not in letters:
        letters.append(b)

graph = [[] for _ in letters]
indeg = [0 for _ in letters]

for a, b in pairs:
    i = letters.index(a)
    j = letters.index(b)
    graph[i].append(j)
    indeg[j] += 1

queue = LinkedListQueue()
for i in range(len(letters)):
    if indeg[i] == 0:
        queue.enqueue(i)

result = []
while not queue.is_empty():
    current = queue.dequeue()
    result.append(current)
    for neigh in graph[current]:
        indeg[neigh] -= 1
        if indeg[neigh] == 0:
            queue.enqueue(neigh)

if len(result) < len(letters):
    print("Противоречие!")
else:
    order = [letters[i] for i in result]
    print("Полный порядок:", order[:10])

end = time.time()
print("Время выполнения метода Б:", end - start, "сек")
print()

print("-" * 30)
print("Метод 2: через collections")
print("-" * 30)

start = time.time()

graph = defaultdict(list)
indeg = defaultdict(int)
all_nodes = set()

for a, b in pairs:
    graph[a].append(b)
    indeg[b] += 1
    all_nodes.update([a, b])

for ch in all_nodes:
    if ch not in indeg:
        indeg[ch] = 0

queue = deque()
for ch in all_nodes:
    if indeg[ch] == 0:
        queue.append(ch)

res = []
while queue:
    curr = queue.popleft()
    res.append(curr)
    for nei in graph[curr]:
        indeg[nei] -= 1
        if indeg[nei] == 0:
            queue.append(nei)

if len(res) < len(all_nodes):
    print("Противоречие!")
else:
    print("Полный порядок:", res[:10])

end = time.time()
print("Время выполнения метода 2:", end - start, "сек")
