
def create_queue():
    return []

def enqueue(queue, new_elem):
    queue.append(new_elem)

def dequeue(queue):
    if len(queue) == 0:
        print('Queue is empty! ')
        return 'Noone'
    return queue.pop(0)

def queue_size(queue):
    return len(queue)


customers = create_queue()
enqueue(customers, 'Alyssa')
enqueue(customers, 'Ben')
enqueue(customers, 'Charlie' )

print(customers)

next = dequeue(customers)

print(f'Next customer: {next}')

next = dequeue(customers)
print(f'Next customer: {next}')

next = dequeue(customers)
print(f'Next customer: {next}')

next = dequeue(customers)

print(customers)