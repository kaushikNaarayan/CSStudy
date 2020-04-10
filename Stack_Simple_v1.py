# Push function
def push_element(element):
	global top
	stack_size = len(s)

	if (top >= stack_size-1):
		return "Stack Overflow" 
	
	s[top+1] = element
	top = top + 1
	print(s)
	print(top)

# Pop function
def pop_top():
	global top
	if (top == -1):
		return "Stack underflow" 
	r = s[top]
	s[top] = 0
	top = top - 1
	return r # returns element that got popped.


print("Welcome to Stack Simple ")

# Assuming Stack size is 3; execute below sequence
s = [0,0,0]
top = -1
push_element(10)
push_element(20)
push_element(30)
c = push_element(40)
print(c)

for each in range(0,4):
	c = pop_top()
	print(c)
