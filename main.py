import plotly
import numpy  as np
import pandas as pd

from time import time

from settings import Settings
from tsp      import Problem

# This is my OWN code written from class notes & references
from solutions.simulated_annealing import simulated_annealing
# This is someone elses dynamic programming solution, for comparison
from python_tsp.exact import solve_tsp_dynamic_programming

def dynamic_programming(problem, settings):
    return solve_tsp_dynamic_programming(problem.distance_matrix)[0]

def main():
    settings = Settings(rng=np.random.default_rng(2022), alpha=0.99, k=1000, repeats=10)
    algs = [('Simulated Annealing', simulated_annealing),
            ('Dynamic Programming', dynamic_programming)]
    i_max = 8; j = 0
    stats = np.zeros(((i_max - 1) * len(algs) * settings.repeats, 4))
    for i in range(1, i_max):
        n_cities = 2*i
        for n in range(settings.repeats):
            problem  = Problem(n_cities=n_cities, size=10)
            for name, algorithm in algs:
                start    = time()
                solution = algorithm(problem, settings)
                end      = time()
                cost     = problem.cost(solution)
                duration = end - start
                stats[j, :] = (n_cities, cost, duration, 1 if 'Dynamic' in name else 0)
                j += 1
                print(f'{name}: {cost:4.6f} in {duration:4.6f} {n_cities:3} cities, repeat {n:3}')
    np.savez('data.npz', stats=stats)

if __name__ == '__main__':
    main()
