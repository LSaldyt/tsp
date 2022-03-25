import plotly.graph_objects as go
import plotly
import numpy  as np
import pandas as pd

from subprocess import call

from utils import *

from solutions.simulated_annealing import simulated_annealing
from main import settings, dynamic_programming, algs, run
from tsp import Problem

def plot_example(problem, solutions, title):
    fig = go.Figure()
    for i, (name, solution) in enumerate(solutions):
        points = problem.points[solution]
        fig.add_trace(go.Scatter(x=points[:, 0], y=points[:, 1],
                                 mode='markers+lines', name=name,
                                 marker=dict(color=QUAL_COLORS[i]),
                                 line=dict(dash=DASH[i])))
    save(fig, 'example', w=1920, h=1080)

def main():
    problem  = Problem(n_cities=16, size=10)
    solutions = []
    for name, algorithm in algs:
        cost, duration, solution = run(algorithm, problem)
        title = f'{name} ({cost:4.4f}, {duration:4.4f}s)'
        solutions.append((title, solution))
    plot_example(problem, solutions, 'test')

if __name__ == '__main__':
    main()
