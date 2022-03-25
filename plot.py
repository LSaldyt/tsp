import plotly.graph_objects as go
import plotly
import numpy  as np
import pandas as pd

from subprocess import call

QUAL_COLORS = plotly.colors.qualitative.G10 + plotly.colors.qualitative.Dark24 + plotly.colors.qualitative.Light24

def save(fig, name, w=1000, h=600, parentdir='data'):
    fig.show()
    fig.write_image(f'{parentdir}/{name}.svg', width=w, height=h)
    fig.write_image(f'{parentdir}/{name}.png', width=w, height=h)
    call(f'rsvg-convert -f pdf -o {parentdir}/{name}.pdf {parentdir}/{name}.svg',
         shell=True)

def main():
    stats = np.load('data.npz')['stats']
    algs  = ('Simulated Annealing', 'Dynamic Programming')
    df    = pd.DataFrame(data=stats,
                         columns=['n_cities', 'cost', 'duration', 'algorithm'])
    fig = go.Figure()
    for i, alg in enumerate(algs):
        sub = df[df['algorithm'] == i]
        fig.add_trace(go.Scatter(x=sub['cost'], y=sub['duration'],
                                 marker=dict(color=QUAL_COLORS[i]),
                                 mode='markers',
                                 name=alg))
    fig.update_layout(
        font=dict(family='Times', size=14, color='black'),
        xaxis_title='Cost',
        yaxis_title='Duration',
        legend=dict(
            orientation="h",
            yanchor='top',
            y=1.0,
            xanchor='center',
            x=0.5,
            bgcolor='white',
            bordercolor='black',
            borderwidth=1),)
    save(fig, 'comparison', w=1920, h=1080)

if __name__ == '__main__':
    main()
