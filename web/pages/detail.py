import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from matplotlib.figure import Figure
from streamlit_player import st_player
from utils.charts import radar_chart
from utils.tennis import Court, CourtDrawer


def main():
    st.title("2021.09.22 シングルス vs高草木")

    # Embed a youtube video
    # https://github.com/okld/streamlit-player/blob/main/streamlit_player/__init__.py
    st_player("https://www.youtube.com/watch?v=f0TX2chsjCo")

    memo = st.text_area(label='振り返りメモ', value='竹安の逆クロスフォアを封じたのが勝因')

    st.markdown("# 基礎分析")    

    st.markdown("## スタッツ")
    df_stats = pd.DataFrame(
        data=[[50, 35, 2, 13, 70, 60], [30, 20, 5, 5, 66, 45], [0, 0, 0, 0, 55, 120], [0, 0, 0, 0, 90, 75]],
        index=['ストローク / フォア', 'ストローク / バック', 'サーブ / 1st', 'サーブ / 2nd'],
        columns=['総本数', 'IN', 'OUT', 'NET', '成功率(%)', '平均球速(km/h)']
    )
    st.table(df_stats.style.highlight_max(axis=0))

    st.markdown("## 過去の自分との比較")
    col1, col2, col3 = st.columns(3)
    col1.metric("平均球速 / ストローク", "70 km/h", "15km/h")
    col2.metric("平均球速 / サーブ / 1st", "90 km/h", "-10km/h")
    col3.metric("平均球速 / サーブ / 2nd", "65 km/h", "5km/h")

    st.markdown("## ハイライト")
    st.markdown("*ストロークのみ抽出*")
    st_player("https://youtu.be/V2cLd0dlK9c")

    st.markdown("*サーブのみ抽出*")
    st_player("https://youtu.be/Bny-NvJ37Ys")

    st.markdown("# 応用分析")
    # st.markdown("### あなたのプレースタイル")
    # radar_chart_fig = radar_chart(5)
    # st.plotly_chart(radar_chart_fig)

    # st.markdown("### 試合の勝因・敗因")

    # st.markdown("### 配球")
    # drawer = CourtDrawer(figsize=(2, 4))
    # court = Court()
    # drawer.draw_court(court)
    # st.pyplot(drawer.fig)

    st.markdown("## ポジショニング")
    delta_position = [0.7137955092961121, 0.37807245801362654, 2.4210657555918416, 0.016460386036984076, 1.122227570381725, -0.38947332907521304, 0.12242060365457919, -0.23349294180040836, 0.11226817920344079, 0.48247834597017913, -0.37675182757591186, 0.690866151557576, 1.177079369165455, 1.3156731887119277, 0.7590291350132228, -0.22287401029824938, 0.5721059635376742, 0.16148533161006107, -0.2289500765234349, -0.15091458630885457, 0.6480613785170162, 1.289655934165082, 1.3332246479179073, 0.6994460702139071, 1.3582352922942835, 2.2704272711567497, -0.06588183696464434, 0.48558816612810496, 0.40086317990191667, 0.5644790050744506, 0.47308929120041743, 0.10518093523158178, 1.5009112464803498, 0.5770888852246134, -0.17653788656583824, 0.8019665948060322, 1.0746227874005134, 4.053210666062732]
    # fig = Figure()
    # ax = fig.subplots()
    # ax.hist(delta_position, bins=25, rwidth=0.9, color='#00a1e9')
    # ax.set_xlabel("Distance(m)")
    # ax.set_ylabel("Number of Shots")
    # st.pyplot(fig)
    fig = px.histogram(delta_position, nbins=25, labels={"value": "正しいポジションからの誤差(メートル)"}, title="正しいポジションとの誤差のヒストグラム")
    fig.update_layout(bargap=0.1)
    st.plotly_chart(fig)

    st_player("https://youtu.be/RuteX6GvuB8")
