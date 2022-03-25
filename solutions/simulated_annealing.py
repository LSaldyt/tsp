import numpy as np

def temperature(T, settings, t):
    return T * settings.alpha**t # Exponential decay

def acceptance_probability(es, en, T):
    if en < es:
        return 1.
    else:
        return np.exp(-(en - es) / T) # Kirkpatrick et. al, MH

def simulated_annealing(problem, settings):
    # TODO vectorize for n solutions w/ different hyperparameters at once
    s = problem.initial(settings.rng)
    T = 1. # Whatever, let's see what happens
    for ki in range(settings.k):
        T = temperature(T, settings, 1 - (ki + 1) / settings.k)
        n = problem.neighbor(s, settings, T)
        es = problem.cost(s); en = problem.cost(n);
        if acceptance_probability(es, en, T) > settings.rng.random():
            s = n
        print(es, s, T, ki)
