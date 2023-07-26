class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None  # First is the Tail of the Linkedlist
        self.last = None  # Last is the Head of LinkedList
        self.length = 0

    def enque(self, value):
        newNode = Node(value)
        self.length += 1
        if self.first == None:
            self.first = newNode
            self.last = newNode
            return True
        self.first.next = newNode
        self.first = self.first.next
        return True

    def dequeue(self):
        if self.last == None:
            return None
        temp = self.last
        self.last = self.last.next
        temp.next = None
        self.length-=1
        if self.last==None:
            self.first=None
        return temp

def main():
    myQueue=Queue()
    while 1:
        n=int(input("1.Enque into Queue\n2.Dequeu from Queue.\n3.Exit....\n"))
        if n==1:
            myQueue.enque(int(input()))
        if n==2:
            poppedValue=myQueue.dequeue()
            print("Dequeued Value is "+str(poppedValue.value) if poppedValue else "Nothing in Queue")
        if n==3:
            print("------------Exiting------------")
            return 0

main()
