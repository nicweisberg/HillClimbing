
def random_guessing(problem, limit):
    """
    Solve the problem by proposing random states, always keeping the
    best state seen so far.
    """

    count = 0
    # grab a random state to start with
    best_guess = problem.random_state()
    
    while count < limit:
        # propose a new random state
        guess = problem.random_state()
        count += 1

        # remember if it's better
        if guess.is_better_than(best_guess):
            best_guess = guess

    # return the best one
    return best_guess


def random_search(problem, limit):
    """
    Solve the problem by making a random change to the current state.
    Keep it if it the random change is better.
    """

    count = 0
    # grab a random state to start with
    best_guess = problem.random_state()
    
    while count < limit:
        # ask for a random change to the current state
        guess = problem.random_step(best_guess)
        count += 1

        # keep it if it is better
        if guess.is_better_than(best_guess):
            best_guess = guess

    # return the best one
    return best_guess


def hillclimbing(problem, limit):
    """
    Solve a problem by taking the biggest uphill step at every state.
    Stop when there are no uphill steps, or you reached the limit.
    """

    count = 0

    # grab a random state to start with
    best_guess = problem.random_state()

    while count < limit:
        # ask for the best state one step away from the current state
        best_neighbour = problem.best_step(best_guess)
        count += 1

        # if the best step is worse than the current state, stop looking (local maximum)
        if best_guess.is_better_than(best_neighbour):
            return best_guess
        # if the best step is equal to the current one, stop looking (plateau)
        elif best_neighbour.is_equal_to(best_guess):
            return best_guess
        # if the best step is uphill, remember it
        else:
            best_guess = best_neighbour

    # return the best one
    return best_guess


def stochastic_hillclimbing(problem, limit):
    """
    Solve a problem by taking a random uphill step at every state.
    Stop when there are no uphill steps, or you reached the limit.
    """

    count = 0

    # grab a random state to start with
    best_guess = problem.random_state()

    while count < limit:
        # ask for a state that's better, chosen at random from the better states
        selection = problem.random_better(best_guess)
        count += 1

        # if a better state could not be found, stop looking
        if selection is None:
            return best_guess
        else:
            # remember the better one
            best_guess = selection

    # return the best one
    return best_guess


def random_restart(problem, rstarts=10, limit=10, stochastic=False):
    """
    Repeat hill-climbing by starting at several random locations.
    """

    # do hill-climbing the first time,
    if stochastic:
        do_HC = stochastic_hillclimbing
    else:
        do_HC = hillclimbing
    
    best_guess = do_HC(problem, limit)

    for r in range(rstarts):
        # try again, maybe it's better?
        g = do_HC(problem, limit)

        # if it's better, remember it
        if g.is_better_than(best_guess):
            best_guess = g

    # return the best one
    return best_guess
