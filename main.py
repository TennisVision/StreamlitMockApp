import streamlit as st

from utils.multi_app import MultiApp


def know_myself():
    st.title("自分を知る")
    # option = st.selectbox(
    #     '自分で積極的にポイントを取りにいくタイプですか？',
    #     (
    #         'Yes', 'No'
    #     )
    # )
    # st.write('You selected:', option)
    q1 = st.checkbox('積極的にポイントを取りにいくタイプである')
    q2 = st.checkbox('ボレーでポイントを取ることが多い')
    q3 = st.checkbox('粘り強く相手のミスを待つ')
    q4 = st.checkbox('相手のミスを待ちつつネットプレーも行う')
    if st.button('タイプ診断'):
        st.write('あなたはフェデラータイプです！')
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8e/Roger_Federer_%2826_June_2009%2C_Wimbledon%29_3_cropped.jpg/344px-Roger_Federer_%2826_June_2009%2C_Wimbledon%29_3_cropped.jpg')

        st.write("次は相手を知りましょう")

def know_opponent():
    st.title("相手を知る")
    q1 = st.checkbox('積極的にポイントを取りにいくタイプである')
    q2 = st.checkbox('ボレーでポイントを取ることが多い')
    q3 = st.checkbox('粘り強く相手のミスを待つ')
    q4 = st.checkbox('相手のミスを待ちつつネットプレーも行う')
    if st.button('タイプ診断'):
        st.write('相手はナダルタイプです！')
        st.image('https://images.tennismagazine.jp/media/article/876/images/main_c84f510490e74d038113cf7d0086537a12503c48.jpg')

        st.write("フェデラータイプ x ナダルタイプの戦略を確認をしましょう")

def lose_pattern():
    st.title("負け筋を知る")
    

app = MultiApp()
app.add_app("自分を知る", know_myself)
app.add_app("相手を知る", know_opponent)
app.add_app("負け筋を知る", lose_pattern)
app.run()