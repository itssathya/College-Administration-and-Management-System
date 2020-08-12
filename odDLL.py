import DBMSTest as dbt
class Node:
    def __init__(self,ele):
        self.element=ele
        self.next=None
        self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def enqueueDLL(self,ele):
        newnode=Node(ele)
        if self.head==None:
            self.head=newnode
        else:
            pos=self.head
            while pos.next!=None:
                pos=pos.next
            pos.next=newnode
            newnode.prev=pos
    def dequeueDLL(self):
        if self.head==None:
            print("Empty")
        elif self.head.next==None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None
    def displayDLL(self):
        if self.head==None:
            print("Empty")
        else:
            pos=self.head
            while pos!=None:
                print(pos.element)
                pos=pos.next
d=DLL()
data=dbt.ODRetrieve()
for i in data:
    d.enqueueDLL(i)

    
      

        
