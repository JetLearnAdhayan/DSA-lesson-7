class Stack:
    def __init__(self, n):
        self.n = n
        self.stack = []

    def push(self, k):
        if len(self.stack) < self.n:
            self.stack.append(k)

        else:
            print("The stack is full.")    
       
    def pop(self):

        if len(self.stack) == 0:
            print("The stack is empty")   
        else:
            self.stack.pop(-1)

    def topstack(self):
        if len(self.stack) == 0:
            print("The stack is empty")
        else:
            print(self.stack[-1])    

    def size(self): 
        if len(self.stack) == 0:
            print("The stack is empty")
        else:
            print(len(self.stack))          

    def display(self):
        print(self.stack)


s = Stack(5)

s.size()
s.push(5)
s.push(2)
s.push(10)
s.push(21)
s.push(7)
s.display()
s.push(5)
s.pop()
s.display()
s.topstack()
s.pop()
s.pop()
s.pop()
s.pop()
s.display()
s.pop()
        