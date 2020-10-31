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
   
jail = set() #indices of particles that have already been detected as collided
newjail = set()

#  10000 steps is definitely enough for AOC. You can probably safely lower it to 1000
for step in range(1000):
    for i in particles:
        i.step()
    #Are there any colisions? Looks wasteful but is still HUGELY faster than the n^2 full collision detection
    if len(particles) != len(set([str(j.pos) for j in particles])):
        for outer in range(0, len(particles)):
            for inner in range(outer + 1, len(particles)):
                if (particles[outer].pos == particles[inner].pos):
                    newjail.add(outer)
                    newjail.add(inner)
        particles = [particles[i] for i in range(len(particles)) if i not in newjail]
        newjail.clear()
particles.sort()

print(len(particles) - len(jail))
# 542 too high