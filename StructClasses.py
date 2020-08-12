class Queue:
    def __init__(self):
        self.list=[]
    def enqueue(self,ele):
        self.list.append(ele)
    def dequeue(self):
        if self.list==[]:
            return "Empty"
        else:
            return self.list.pop(0)
class Stack:
    def __init__(self):
        self.list=[]
    def push(self,ele):
        self.list.append(ele)
    def pop(self):
        if self.list==[]:
            return "Empty"
        else:
            return self.list.pop()
    def peek(self):
        return self.list[-1]
