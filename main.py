import plotly
import numpy  as np
import pandas as pd

from settings import Settings
from tsp      import Problem
from solutions.simulated_annealing import simulated_annealing

def main():
    settings = Settings(rng=np.random.default_rng(2022), alpha=0.99, k=1000)
    problem  = Problem(n_cities=10, size=10)
    simulated_annealing(problem, settings)

if __name__ == '__main__':
    main()
