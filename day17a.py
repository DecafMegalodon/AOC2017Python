#  https://adventofcode.com/2017/day/17
import fileinput

class LLnode:
    def __init__(self, data, nextnode = None):
        self.data = data
        self.nextnode = nextnode
        
class CircLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    '''Inserts the data in a new node in front of the current head'''
    def insert(self, data):
        if self.head != None:
            self.head.nextnode = LLnode(data, self.head.nextnode)
        else:
            self.head = LLnode(data)
            self.head.nextnode = self.head
        self.size += 1

    def advance(self, amount = 1):
        if self.head != None:
            for i in range(amount, 0, -1):
                self.head = self.head.nextnode
                
    '''Seeks the circular LL to the 'first' instance of the target after the current index, if any.
        Does nothing if it's not found'''
    def seek(self, target):
        if self.head != None:
            curNode = self.head.nextnode
            while curNode.data != target and curNode != self.head:
                curNode = curNode.nextnode
            self.head = curNode
            
    def __str__(self):
        if self.head ==  None:
            return "None"
        else:
            origNode = self.head
            curNode = origNode.nextnode
            strRep = ">" + str(origNode.data) + "< -> "
            while curNode != origNode:
                strRep += str(curNode.data) + " -> "
                curNode = curNode.nextnode
            return strRep
        
ll = CircLinkedList()
puzInput = int(fileinput.input().readline().strip("\n"))

for i in range(2017+1):
    ll.insert(i)
    ll.advance(1 + puzInput)
ll.seek(2017)
ll.advance()
print(ll.head.data)