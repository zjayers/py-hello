from collections import deque

queue = deque([])

#  Add Items To Stack
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

# Remove last item in stack
firstItemInQueue = queue.popleft()
print(queue)

# Check if stack is empty
if not queue:
    print("empty")
