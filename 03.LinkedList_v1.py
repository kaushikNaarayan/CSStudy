class node:
	
	#Node Init
	def __init__(self, value):
		self.value = value
		self.next = None


class linked_list:
	def __init__(self):
		self.head = None	

	# Datageneration method; Used only for Testing below functions
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


	def append(self,value):
		node_new = node(value)
		node_new.next = None
		
		self.head= node_new

#Create List			
llist = linked_list()

#Generate Curve
llist.init_generate(10)
llist.getData()

#Push Header
llist.push(1000)
llist.getData()
print(llist.head.value)

Push End

