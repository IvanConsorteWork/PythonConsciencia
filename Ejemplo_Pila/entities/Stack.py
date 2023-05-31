#%%
class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return True if len(self.stack) == 0 else False
    
    def push(self,item):
        self.stack.append(item)
    
    def pop(self):
        return None if self.isEmpty() else self.stack.pop()
    
    def peek(self):
        return None if self.isEmpty() else self.stack[-1]

pila = Stack()
pila.push(1)
print(pila.stack)

        
# %%
