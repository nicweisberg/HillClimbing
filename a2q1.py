import machine as machine
import math as Math
import random as random

class State(object):
    """  A State object stores a potential solution to a search problem.
         Its two methods are needed by localsearch.py
    """
    
    def __init__(self, object):
        
        self.sequence = object[0]
        self.entries = object[1:len(object)]
        
        pass

    def is_better_than(self, other):
        """ 
            Return True if self is a better solution than other
        """
        if Problem.objective_function(self, self) < Problem.objective_function(self, other):
            return True
        
        return False

    def is_equal_to(self, other):
        """ 
            Return True if self is as good a solution as other
        """
        if Problem.objective_function(self, self) == Problem.objective_function(self, other):
            return True
            
        return False


class Problem(object):
    """  A Problem object implements the methods needed by the
         algorithms in localsearch.py
    """

    def __init__(self, object):
        self.possible_operators = ["NOP","ADD","MUL","SUB","DIV"]
        self.sequenceLength = len(object.sequence)
        self.entries = object.entries
        pass
    

    def objective_function(self, state):
        """
            Returns the objective value of the given state.
        """
        value = 0
        
        for entry in state.entries:
            value = value + (entry[0]-machine.machine_exec(state.sequence, entry))**2
        
        value = value / len(state.sequence)
        value = Math.sqrt(value)
        
        
        
        return value


    def random_state(self):
        """ Return a random State, completely independent of any other State.
        """
        newState = []
        newSequence = []
        for each in range(0,self.sequenceLength):
            newSequence.append(self.possible_operators[random.randrange(5)])
        
        newState.append(newSequence)
        newState = newState + self.entries
        return State(newState)

    def random_step(self, state):
        """ Return a State that is a random neighbour of the given State.
        """
        randomOperator = self.possible_operators[random.randrange(5)]
        randomPlacement =  random.randrange(self.sequenceLength)
        newSequence = state.sequence
        newSequence[randomPlacement] = randomOperator
        newState = []
        newState.append(newSequence)
        newState = newState + state.entries
       
        
        return State(newState)


    def best_step(self, state):
        """ Return the best neighbouring State for the given State
        """
        min = 0
        for operator in self.possible_operators:
            for index in range(self.sequenceLength):
                newState = []
                newSequence = state.sequence.copy()
                newSequence[index] = operator
                newState.append(newSequence)
                newState = newState + state.entries
                newState = State(newState)
                obj_func = self.objective_function(newState)
                if (obj_func < min) or (min==0):
                    min = obj_func
                    bestState = newState
        return bestState


    def random_better(self, state):
        """ Return a State that is a random BETTER neighbour of the given State.
        """
        
        obj_func = self.objective_function(state)
        
        randomOperator = self.possible_operators[random.randrange(5)]
        randomPlacement =  random.randrange(self.sequenceLength)
        newSequence = state.sequence
        newSequence[randomPlacement] = randomOperator
        newState = []
        newState.append(newSequence)
        newState = newState + state.entries
        if self.objective_function(State(newState)) < obj_func:
            return State(newState)
        else:
            return self.random_better(state)



