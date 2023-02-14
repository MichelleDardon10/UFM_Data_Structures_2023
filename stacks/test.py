from stack import Stack

# Stack initialization
stack = Stack(5)
print(stack)

# Push first element METER
stack.push('A')

# Other pushes
stack.push('B')
print(stack)
stack.push('C')
print(stack)
stack.push('D')
print(stack)
stack.push('E')
print(stack)
# stack.push('F') # Forces stack overflow

# Pops SACAR
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
# stack.pop() # Forces stack underflow

# Peek BUSCAR
stack.push('D')
stack.push('C')
print(stack)
print('Peek: ', stack.peek())
stack.push('E')
print(stack)
print('Peek: ', stack.peek())
