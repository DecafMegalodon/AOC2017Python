#  https://adventofcode.com/2017/day/20
import fileinput

class particle:
    def __init__(self, description):
        splitline = description.split('>')[:3]
        splitline = [component.strip(', pva=<') for component in splitline]
        self.pos = [int(i) for i in splitline[0].split(',')]
        self.vel = [int(i) for i in splitline[1].split(',')]
        self.acc = [int(i) for i in splitline[2].split(',')]
        self.dist = self.distance()
        
    def distance(self):
        return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        

    def __lt__(self, other):
        return self.distance() < other.distance()
        
    def __str__(self):
        return f"Pos: {self.pos} Vel: {self.vel} Acc: {self.acc} dist: {self.dist}"

particles = []

for line in fileinput.input():
    particles.append(particle(line))

particles.sort()    

for i in particles:
    print(i)
    
