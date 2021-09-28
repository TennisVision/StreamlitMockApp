import numpy as np
import pandas as pd
import plotly.express as px


def radar_chart(val):  
    df = pd.DataFrame(dict(
        r=[
            np.random.randint(1,val),
            np.random.randint(1,val),
            np.random.randint(1,val),
            np.random.randint(1,val),
            np.random.randint(1,val),
            np.random.randint(1,val)
        ],
        theta=[
            'ストローク / フォアハンド',
            'ストローク / バックハンド',
            'サーブ / 1st',
            'サーブ / 2nd',
            'ボレー / フォアハンド',
            'ボレー / バックハンド',
        ]
    ))
    fig = px.line_polar(df, r='r', theta='theta', line_close=True)
    return fig
