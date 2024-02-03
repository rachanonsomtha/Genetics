import random

def cost_function(x, y, z):
    return x + y + z


def calculate_fitness_score(x , y, z):
    ans = cost_function(x, y, z)
    return 1 / (0.0001  + ans)

#generate solutions
solutions = []
for sol in range(1000):
    ##replace this one with parameters
    x = random.uniform(0, 1000)
    y = random.uniform(0, 1000)
    z = random.uniform(0, 1000)

    solutions.append((x, y, z))
    

itterationCount = 10000
# replace this with number of 
for i in range(itterationCount):
    
    rankedSolutions = []
    for sol in solutions:
        rankedSolutions.append((calculate_fitness_score(sol[0], sol[1], sol[2]), sol))
    # sort solution in some ways
    rankedSolutions.sort()
    rankedSolutions.reverse()
    
    print (f"=== Gen {i} best solutions === ")
    print (rankedSolutions[0])
    
    #stop if solution is sastisfied
    if (rankedSolutions[0][0] > 1000):
        break
    
    #get top 100 solutions in the solutions set
    bestSolutions = rankedSolutions[:100]
    
    elements = []
    for s in bestSolutions:
        elements.append(s[1][0])
        elements.append(s[1][1])
        elements.append(s[1][2])
        
    newGeneration = []
    for _ in range(itterationCount):
        #generate new element for new generation and mutate
        ele1 = random.choice(elements) * random.uniform(0.99, 1.01)
        ele2 = random.choice(elements) * random.uniform(0.99, 1.01)
        ele3 = random.choice(elements) * random.uniform(0.99, 1.01)
        
        newGeneration.append((ele1, ele2, ele3))
        
    solutions = newGeneration
    

