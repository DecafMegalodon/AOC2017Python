#  https://adventofcode.com/2017/day/20
import fileinput

class particle:
    def __init__(self, pos, vel, acc):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.dist = self.distance()
        
    def distance(self):
        return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        

    def __lt__(self, other):
        return self.distance() < other.distance()
        
speck = particle([1,1,1], [], [])
print(speck.dist)