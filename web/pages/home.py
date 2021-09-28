import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from streamlit_player import st_player


def create_radar_chart(val):  
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

def create_movie_row(id: int, video: str, title: str, date: str, score: str):
    container = st.container()
    with container:
        col1, col2, col3, col4 = st.columns([4, 1, 1, 1])
        with col1:
            if id==-1:
                st.write("動画")
            else:
                st_player(video, key=id)
        with col2:
            st.write(title)
        with col3:
            st.write(date)
        with col4:
            st.write(score)


def main():
    st.markdown("# Tennis Vision")
    container1 = st.container()
    with container1:
        st.markdown("## プロフィール")
        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.image("https://celeby-media.net/file/parts/I0000732/a65ee92f1a0117ffad0e004908434642.jpg")
            st.markdown("### Roger Federer")
        with col2:
            st.metric("戦略レベル", "75", "15")
        with col3:
            st.metric("技術レベル", "60", "10")
            # radar_chart_fig = create_radar_chart(5)
            # st.plotly_chart(radar_chart_fig)
    
    container2 = st.container()
    with container2:
        st.write("## スタッツ推移")
        chart_data = pd.DataFrame(
            np.random.randint(0, 100, (10, 4)),
            columns=['成功率/ストローク/フォア', '成功率/ストローク/バック', '成功率/サーブ/1st', '成功率/サーブ/2nd']
        )
        st.line_chart(chart_data)

    container3 = st.container()
    with container3:
        st.write("## 動画一覧")
        create_movie_row(-1, "動画", "タイトル", "日付", "スコア")
        create_movie_row(str(1), "https://www.youtube.com/watch?v=f0TX2chsjCo", "本郷杯シングルス", "2021.09.21", "6-4")
        create_movie_row(str(2), "https://youtu.be/LWLlmzUYQPg", "農学部オムニ", "2021.09.21", "6-2")
        create_movie_row(str(3), "https://youtu.be/ZcCKKpLarM4", "接戦 vs開", "2021.09.21", "5-7")
