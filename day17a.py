#  https://adventofcode.com/2017/day/16
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

    def advance(self):
        if self.head != None:
            self.head = self.head.nextnode
            
    def __str__(self):
        if self.head ==  None:
            return "None"
        else:
            origNode = self.head
            curNode = origNode.nextnode
            strRep = ">" + str(origNode.data) + "<  -> "
            while curNode != origNode:
                strRep += str(curNode.data) + " -> "
                curNode = curNode.nextnode
            return strRep
        
ll = CircLinkedList()
ll.insert("Moo")
ll.insert("Boo")
ll.insert("Voodoo")
print(ll)