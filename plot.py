import plotly.graph_objects as go
import plotly
import numpy  as np
import pandas as pd

from utils import *

def main():
    stats = np.load('data.npz')['stats']
    algs  = ('Simulated Annealing', 'Dynamic Programming')
    df    = pd.DataFrame(data=stats,
                         columns=['n_cities', 'cost', 'duration', 'algorithm'])

    comparisons = [('n_cities', 'duration'),
                   ('n_cities', 'cost'),
                   ('cost',     'duration')]

    for x, y in comparisons:
        fig = go.Figure()
        for i, alg in enumerate(algs):
            sub = df[df['algorithm'] == i]
            fig.add_trace(go.Scatter(x=sub[x], y=sub[y],
                                     marker=dict(color=QUAL_COLORS[i]),
                                     mode='markers',
                                     name=alg))
        fig.update_layout(
            xaxis_title=x.title(),
            yaxis_title=y.title())
        if y == 'duration':
            fig.update_yaxes(type='log')
        save(fig, f'comparison_{x}_{y}', w=1920, h=1080)

if __name__ == '__main__':
    main()
