import streamlit as st

from utils.multiapp import MultiApp
from pages import home, detail, tomato

# def home():
#     st.markdown("# Home")

if __name__=="__main__":
    st.set_page_config(layout="wide")
    app = MultiApp()

    # Add all your application here
    app.add_app("ホーム", home.main)
    app.add_app("詳細", detail.main)
    app.add_app("トマトツリー", tomato.main)

    # The main app
    app.run()
