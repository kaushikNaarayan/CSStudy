class node:
	
	#Node Init
	def __init__(self, value):
		self.value = value
		self.next = None


class linked_list:
	def __init__(self):
		self.head = None	

	# Data generation method; Used only for Testing below functions
	def init_generate(self,count):

		#initialise List
		
		#Specify Head Position
		llist.head = node(1)

		#loop to create n nodes with values = factors of 10 [10,20,30....]

		node_no = llist.head
		#print(node_no.value, node_no.next)
		e = 2
		while e <= count:
			node_no_new = node(e*10)
			node_no.next = node_no_new 
			node_no = node_no_new
			e+=1
		return llist

	# Retrieval methods
	# Get count of nodes in the linked list

	def getCount(self):
		counter = 0	
		temp = self.head
		while (temp):
			temp = temp.next
			#print(temp,temp.next)
			counter+=1	
		return counter

	def getData(self):
		temp = self.head
		while(temp != None):
			print(temp.value,"|",temp.next)
			temp = temp.next		

	# Modification methods
	# Design: add in beginning - called push; add in-between called insert, add in end called append	
	def push(self,value):
		node_new = node(value)
		node_new.next = self.head
		self.head= node_new
	
	def node_position(self,node):
		n = self.head
		counter = 0
		while(n!=node):
			n = n.next
			counter+=1
		return counter
				

	def remove(self,position):
		
		llist_size = self.getCount()
		if (position > llist_size -1) or (position < 0):
			print("Position out of range")
			return None
			
		# cases: head, tail and mid
		#head case
		if position == 0:
			self.head = self.head.next
		#tail case	
		elif position == llist_size -1:
			temp = self.head
			while(temp.next):
				temp_prev = temp
				temp = temp.next
				
			temp_prev.next = None

		#mid case
		else: 
			temp = self.head
			counter = 0
			while(counter != position):
				
				temp_prev = temp
				temp = temp.next
				counter+=1

			temp_next = temp.next	
			temp_prev.next = temp_next
		
		print("position ", position, " has been removed from the linked list")
						

#Create List			
llist = linked_list()

#Generate Curve
llist.init_generate(10)
#llist.getData()

#Push Header
llist.push(1000)
#llist.getData()
#print(llist.head.value)

#remove node
llist.getCount()
llist.remove(10)

llist.getData()
print(llist.head.value)