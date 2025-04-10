from array import array

def create_queue():
    return array('i')

def enqueue(queue, new_elem):
    queue.append(new_elem)

def deque(queue):
    return queue.pop(0)


def queue_size(queue):
    return len(queue)

numbers = create_queue()

enqueue(numbers, 17)
print(numbers)

enqueue(numbers, 24)

enqueue(numbers, 30)
print(numbers)

next = deque(numbers)
print(f'Next: {next}')

next = deque(numbers)
print(f'Next: {next}')

print(numbers)

