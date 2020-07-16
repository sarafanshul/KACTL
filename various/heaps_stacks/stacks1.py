# # -------Stack Data Structure---------
'''
stack are just like lists but we can custamize it
'''

# # balencing parentheses example

# class Stack():
	
# 	def __init__(self):
# 		self.items = []

# 	def push(self , *item):
# 		# self.items.extend(item)
# 		self.items += item

# 	def pop(self):
# 		return self.items.pop()

# 	def peek(self):
# 		if not self.is_empty():
# 			return self.items[-1]

# 	def get_stack(self):
# 		return self.items

# 	def is_empty(self):
# 		return self.items == []

from stacks import Stack

def is_match(p1 , p2):
	if p1 == p2:
		return True
def is_balenced(par_str):
	s = Stack()
	is_balenced = True
	index = 0

	while index < len(par_str) and is_balenced:
		par = par_str[index]
		if par in '({[':
			s.push(par)
		else:
			if s.is_empty():
				is_balenced = False
			else:
				top = s.pop()
				if not is_match(top , par):
					is_balenced = False
		index += 1
	if s.is_empty() and is_balenced:
		return True

print(is_balenced('{{}}'))

	
