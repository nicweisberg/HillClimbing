# HillClimbing
 Comparing local search algorithms


Hill climbing is a local search algorithm that works by attempting to optimize its current state. We call it "hill climbing" because at every point in a graph traversal it evaluates the quality of its current state and then attempts to "move up hill" by performing an action that results in a state with a higher quality. The measure of quality of states is different for every problem, and is evaluated by something called an objective value function.

One downside to hill climbing is the fact that it is not guarunteed to find an optimal solution. This is due to the possibility of a search space having local maximums that the search gets trapped in. Taking a look at the picture on the bottom right, you can imagine how the current state will reach the top of its hill and not be able to climb any further. This problem can be reduced by techniques such as "random restart hillclimbing", where when the search algorithm reaches a maximum, it restarts in a random state in the search space, in the hopes that it will land on a path that leads to a better solution.

I was assigned the task of comparing different hill climbing techniques to a simple optimization problem. The problem was as follows: given a set of m lists of n integers, each list containing a corresponding goal value, attempt to find the sequence of n-1 operators (add, subtract, skip, multiply, divide) such that when the sequence is applied to each list in the set, the resulting expression will be closest to the lists corresponding goal value.
