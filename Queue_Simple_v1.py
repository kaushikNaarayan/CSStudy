#Queue of only natural numbers


#Functions
def enqueue(element):
	global  front,back, queue_size

	if (back >= queue_size-1):	
		return "Queue is full"
	
	queue_array[back+1] = element
	
	back = back + 1
	if(front == -1):
		front = front + 1
	return queue_array

def dequeue():
	global  front,back, queue_size

	if (front == queue_size):
		return "Nothing in queue to remove"
	r = queue_array[front]
	queue_array[front] = 0	
	front = front + 1
	return r

#Variables
queue_array = [0,0,0,0,0]
queue_size = len(queue_array)
front = -1 #can take 0 to queue_size -1
back = -1 # can take -1,0


print(queue_array)

for e in range(0,8):
	c = enqueue(10 + e*10)
	print(c)

for e in range(0,6):
	c = dequeue()
	print(c,queue_array)
