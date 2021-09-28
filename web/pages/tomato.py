import streamlit as st
import pandas as pd

def main():
    my_player_type = None
    opponent_player_type = None
    situation_lose = None
    strategy = None
    tactics = None

    st.title("試合前の戦略・戦術策定支援")

    st.markdown("# タイプ診断")
    # https://docs.google.com/presentation/d/1N3t_ENq_4YE8ew9e2bexysBsGvqFoDPfpDvWdWUpCN0/edit?usp=sharing
    st.image("web/assets/player_type.png", width=800)
    my_player_type = st.selectbox("あなたのタイプを選択してください", ["A", "B", "C", "D"])

    st.markdown("# 戦略策定")
    st.markdown("> テニスの戦略とは, 「自分が得意な展開へ誘導し, 相手の得意な展開を封じること」だと私たちは考えています")
    opponent_player_type = st.selectbox("対戦相手のタイプを選択してください", ["A", "B", "C", "D"])
    if my_player_type and opponent_player_type:
        st.write(f"タイプ{my_player_type}(あなた)がタイプ{opponent_player_type}に負ける展開として一番ありそうなものを選んでください")
        if my_player_type=='A':
            if opponent_player_type=='A':
                situation_lose = st.selectbox(
                    "負け展開を選択してください",
                    [
                        "相手が先にネットプレーする",
                        "自分の上位互換"
                    ]
                )
                if situation_lose=="相手が先にネットプレーする":
                    strategy = "相手をネットに詰めさせない"
                elif situation_lose=="自分の上位互換":
                    strategy = "諦めてください"
            elif opponent_player_type=='B':
                pass
            elif opponent_player_type=='C':
                pass
            elif opponent_player_type=='D':
                pass
        elif my_player_type=='B':
            if opponent_player_type=='A':
                pass
            elif opponent_player_type=='B':
                pass
            elif opponent_player_type=='C':
                pass
            elif opponent_player_type=='D':
                pass
        elif my_player_type=='C':
            if opponent_player_type=='A':
                pass
            elif opponent_player_type=='B':
                pass
            elif opponent_player_type=='C':
                pass
            elif opponent_player_type=='D':
                pass
        elif my_player_type=='D':
            if opponent_player_type=='A':
                pass
            elif opponent_player_type=='B':
                pass
            elif opponent_player_type=='C':
                pass
            elif opponent_player_type=='D':
                pass
        
        if strategy:
            st.write(f"「{situation_lose}」にしないために取るべき戦略は「{strategy}」です！")


    st.markdown("# 戦術策定")
    st.markdown("> テニスの戦術とは, 「目指す展開に誘導するために, 作戦AでリスクBを負ってショットCを打つこと」だと私たちは考えています(何言ってるかわからないですよねw)")
    if strategy:
        st.write(f"「{strategy}」の展開に誘導するための戦術は以下のようになります")
        if strategy=="相手をネットに詰めさせない":
            df_tactics = pd.DataFrame(
                columns=['作戦A', 'リスクB', 'ショットC'],
                data=[
                    ["早いテンポのラリーにする", "ポジション", "ライジング"],
                    ["早い球速のラリーにする", "球速", "強打"],
                    ["相手がよくアプローチに使うショットを使わせない", "コース", "コントロールしやすいショット"]
                ]
            )
            st.table(df_tactics.set_index("作戦A"))
