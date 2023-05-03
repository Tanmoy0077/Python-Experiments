class Heap_MAX:
    def __init__(self, l = []):
        self.data = l
        self.build_max_heap(len(self.data))

    def max_heapify(self, i, n):
        left = 2*i + 1
        right = 2*i + 2
        max_i = i
        if left < n and self.data[left] > self.data[i]:
            max_i = left
        if right < n and self.data[right] > self.data[max_i]:
            max_i = right
        if max_i != i:
            self.data[i], self.data[max_i] = self.data[max_i], self.data[i]
            self.max_heapify(max_i, n)
        
    def build_max_heap(self, n):
        for i in range(int(n/2), -1, -1):
            self.max_heapify(i, n)
    
    def del_max(self):
        if self.data:
            temp = self.data[0]
            self.data[0] = self.data[-1]
            del(self.data[-1])
            self.max_heapify(0, len(self.data))
            return temp

    def insert(self, val):
        self.data.extend([val])
        self.build_max_heap(len(self.data))
    
    def __str__(self):
        return f"{self.data}"

if __name__ == '__main__':
    h1 = Heap_MAX([1,2,5,6,9,7])
    print(h1)
    print(h1.del_max())
    print(h1)
    print(h1.del_max())
    print(h1)
    print(h1.del_max())
    print(h1)
    print(h1.del_max())
    print(h1)
    print(h1.del_max())
    print(h1)
    print(h1.del_max())
    h1.insert(10)
    h1.insert(3)
    h1.insert(7)
    print(h1)
    
