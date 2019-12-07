import localsearch as Search
import a2q1 as problem
import time as time


def parseSciNot(element):
    element = element.split('e')
    value = float(element[0])
    exponent = int(element[1])
    return (10**exponent)*value
    
def buildSciNot(number):
    exponent = 0 
    number = str(number).split(".")
    if number[0] == "0":
        i = 0
        while number[1][i]=="0":
            exponent = exponent-1
            i = i + 1
        number = number[1][i:i+4]
        number = number[0]+"."+number[1:4]+"e"+str(exponent)
    return number
    



print()
print()
print()
print("////////////       Local Search        ////////////")
print("////////////      Nick Weisberg       ////////////")
print()
print()
inputFile = input("Which input file would you like to read from? (small, moderate, morelines, harder, longscript, largerange) ")
print()
print("Reading files from "+inputFile+".txt: ")
print()
print("Goal Value    |      Operands")
print()


initialState = []
file = open(inputFile+".txt", "r")
lines = file.readlines()
n = 0
for line in lines:
    if n!=0:
        print(line)
        line = line.strip()
        line = line.split(" ")
        entry = []
        for element in line:
            if line.index(element)==0:
                entry.append(parseSciNot(element))
            else:
                entry.append(float(element))
        initialState.append(entry)
    else:
        initialSequence = []
        line = line.strip()
        line = line.split(" ")
        for i in range(0,int(line[1])):
            initialSequence.append("ADD")
        initialState.append(initialSequence)
    n = n + 1

state = problem.State(initialState)
initialProblem = problem.Problem(state)

for steps in [1000,2000,4000,8000]:

    print("Random Guessing @ "+str(steps)+" Steps:")
    start_time = time.time()
    solution = Search.random_guessing(initialProblem, steps)
    print(solution.sequence)
    print(str(time.time()-start_time) + " seconds")
    print('%.5E' % problem.Problem.objective_function(solution, solution))
    
    print("Random Search @ "+str(steps)+" Steps:")
    start_time = time.time()
    solution = Search.random_search(initialProblem, steps)
    print(solution.sequence)
    print(str(time.time()-start_time) + " seconds")
    print('%.5E' % problem.Problem.objective_function(solution, solution))
    
    print("Hill Climbing @ "+str(steps)+" Steps:")
    start_time = time.time()
    solution = Search.hillclimbing(initialProblem, steps)
    print(solution.sequence)
    print(str(time.time()-start_time) + " seconds")
    print('%.5E' % problem.Problem.objective_function(solution, solution))
    
    print("Stochastic Hillclimbing @ "+str(steps)+" Steps:")
    start_time = time.time()
    solution = Search.stochastic_hillclimbing(initialProblem, steps)
    print(solution.sequence)
    print(str(time.time()-start_time) + " seconds")
    print('%.5E' % problem.Problem.objective_function(solution, solution))
    
    print("Random Restart @ "+str(steps)+" Steps (Var 1):")
    start_time = time.time()
    solution = Search.random_restart(initialProblem, limit=20)
    print(solution.sequence)
    print(str(time.time()-start_time) + " seconds")
    print('%.5E' % problem.Problem.objective_function(solution, solution))

    print("Random Restart @ "+str(steps)+" Steps (Var 2):")
    start_time = time.time()
    solution = Search.random_restart(initialProblem, limit=100)
    print(solution.sequence)
    print(str(time.time()-start_time) + " seconds")
    print('%.5E' % problem.Problem.objective_function(solution, solution))

