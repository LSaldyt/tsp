import numpy as np

def neighbor(s, settings, T):
    return s + settings.rng.normal(loc=0, scale=np.abs(T))

def temperature(T, settings, t):
    return T * settings.alpha**t

def initial(settings):
    return settings.rng.random() * 20. - 10. # -10., 10.

def E(s):
    return s**2

def P(es, en, T):
    if en < es:
        return 1.
    else:
        return np.exp(-(en - es) / T) # Kirkpatrick et. al, MH

def simulated_annealing(problem, settings):
    print('Simulated annealing!', flush=True)
    s = initial(settings)
    T = 1. # Whatever, let's see what happens
    for ki in range(settings.k):
        T = temperature(T, settings, 1 - (ki + 1) / settings.k)
        n = neighbor(s, settings, T)
        if P(E(s), E(n), T) > settings.rng.random():
            s = n
        print(E(s), s, T, ki)
