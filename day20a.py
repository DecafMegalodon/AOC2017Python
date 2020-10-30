#  https://adventofcode.com/2017/day/20
import fileinput

class particle:
    def __init__(self, description, id):
        splitline = description.split('>')[:3]
        splitline = [component.strip(', pva=<') for component in splitline]
        self.pos = [int(i) for i in splitline[0].split(',')]
        self.vel = [int(i) for i in splitline[1].split(',')]
        self.acc = [int(i) for i in splitline[2].split(',')]
        self.dist = self.distance()
        self.id = id
        
    def distance(self):
        return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])
        
    #  Advance the simulation for this particle
    def step(self):
        for i in range(3):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]
        self.dist = self.distance()

    def __lt__(self, other):
        return self.distance() < other.distance()
        
    def __str__(self):
        return f"Pos: {self.pos} Vel: {self.vel} Acc: {self.acc} dist: {self.dist}, id: {self.id}"

particles = []

for line in fileinput.input():
    particles.append(particle(line, len(particles)))
   

#  10000 steps is likely enough for AOC but you may wish to bump it higher
for step in range(10000):
    for i in particles:
        i.step()
particles.sort()

print(particles[0].id)
    
