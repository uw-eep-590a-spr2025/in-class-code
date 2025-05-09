

class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, payload):
        ## Put it in the first open spot
        self.heap.append(payload)

        new_index = len(self.heap) - 1
        parent_index = (new_index - 1) // 2

        ## Min Heap
        while self.heap[parent_index] > self.heap[new_index]:
            print(f'swap {self.heap[parent_index]} to {self.heap[new_index]}')
            tmp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[new_index]
            self.heap[new_index] = tmp
            print(self.heap)

            new_index = parent_index
            parent_index = (new_index - 1) // 2

            if parent_index < 0 or new_index < 0:
                break

            print(f'parent {parent_index} and new {new_index}')

        print(self.heap)

    def extract_min(self):
        out = self.heap[0]
        self.heap[0] = self.heap.pop()

        cur_ind = 0
        left_child = cur_ind * 2 + 1
        right_child = cur_ind * 2 + 2

        swap_ind = left_child if self.heap[left_child] < self.heap[right_child] else right_child

        while self.heap[cur_ind] > self.heap[swap_ind]:
            tmp = self.heap[swap_ind]
            self.heap[swap_ind] = self.heap[cur_ind]
            self.heap[cur_ind] = tmp
            cur_ind = swap_ind
            left_child = cur_ind * 2 + 1
            right_child = cur_ind * 2 + 2

            if right_child > len(self.heap) - 1:
                if left_child > len(self.heap) - 1:
                    break
                else:
                    swap_ind = left_child
            else:
                swap_ind = left_child if self.heap[left_child] < self.heap[right_child] else right_child


        return out

pq = Heap()

pq.insert(42)
pq.insert(36)
pq.insert(100)
pq.insert(12)
pq.insert(15)

print(pq.heap)

min = pq.extract_min()
print(min)

print(pq.heap)









priority_queue = []

def insert_pq(pqueue, element):
    pqueue.append(element)
    pqueue.sort()

def remove_pq(pqueue):
    pqueue.pop(0)