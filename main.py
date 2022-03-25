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

def main():
    settings = Settings(rng=np.random.default_rng(2022), alpha=0.99, k=100)
    for i in range(1, 6):
        n_cities = 2**i
        problem  = Problem(n_cities=n_cities, size=10)
        start    = time()
        approx   = simulated_annealing(problem, settings)
        mid      = time()
        exact, _ = solve_tsp_dynamic_programming(problem.distance_matrix)
        end      = time()
        print(n_cities)
        print('Approximate:', problem.cost(approx), mid - start)
        print('Exact:      ', problem.cost(exact),  end - mid)

if __name__ == '__main__':
    main()
