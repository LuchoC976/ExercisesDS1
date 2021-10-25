class ListNode:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class HashMap:
    def __init__(self):
        self.size = 20000
        self.mult = 12321421
        self.data = [None for _ in range(self.size)]

    def hash(self, key):
        return key * self.mult % self.size

    def put(self, key, value):
        self.remove(key)
        h = self.hash(key)
        node = ListNode(key, value, self.data[h])
        self.data[h] = node

    def get(self, key):
        h = self.hash(key)
        node = self.data[h]
        while node:
            if node.key is key:
                return node.val
            node = node.next

    def remove(self, key):
        h = self.hash(key)
        node = self.data[h]
        if not node:
            return
        if node.key is key:
            self.data[h] = node.next
            return
        while node.next:
            if node.next.key is key:
                node.next = node.next.next
                return
            node = node.next


mapaPrueba = HashMap()
mapaPrueba.put(12, "Primera prueba")
print(mapaPrueba.get(12))
mapaPrueba.put(15, "Segunda prueba")
mapaPrueba.put(121, "Tercera prueba")
mapaPrueba.put(1, "Cuarta prueba")
print(mapaPrueba.get(1))