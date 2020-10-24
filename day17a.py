#  https://adventofcode.com/2017/day/16
import fileinput

class LLnode:
    def __init__(self, data):
        self.data = data
        self.nextnode = None
    def __init__(self, data, nextnode):
        self.data = data
        self.nextnode = nextnode
        
class LinkedList:
    def __ini__(self):
        self.head = None

    '''Inserts the data in a new node in front of the current head'''
    def insert(self, data):
        if self.head != None:
            self.head.nextnode = LLnode(data, self.head.nextnode)
        else:
            self.head = LLnode(data)
            self.head.nextnode = self.head

    def advance(self):
        if self.head != None:
            self.head = self.head.nextnode
            
    def __str__(self):
        return "cats"
        
ll = LinkedList()
print(ll)