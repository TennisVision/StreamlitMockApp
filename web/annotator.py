import os
import sys
from typing import List

import cv2
import numpy as np
import numpy.typing as npt
import pandas as pd
import plotly.express as px
import streamlit as st
# https://github.com/null-jones/streamlit-plotly-events/blob/master/src/streamlit_plotly_events/__init__.py
from streamlit_plotly_events import plotly_events

sys.path.append(
    os.path.abspath((os.path.join(os.path.dirname(__file__), '../', '../')))
)


def get_image(file_id: int, frame_id: int) -> npt.NDArray:
    file_id_str = str(file_id).zfill(4)
    video_path = f'demos/{file_id_str}/{file_id_str}_ann_video.mp4'
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_id)
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    return frame

def get_input_frame_ids() -> List[int]:
    input_frame_ids = st.text_input(label="フレーム番号をカンマ区切りで入力", value="1,2,3")
    input_frame_ids = eval(input_frame_ids)
    if type(input_frame_ids)==int:
        input_frame_ids = [input_frame_ids]
    return input_frame_ids

@st.cache
def get_cached_images(file_id: int, frame_ids: List[int]) -> List[npt.NDArray]:
    images = []
    for frame_id in frame_ids:
        image = get_image(file_id, frame_id)
        images.append(image)
    return images

@st.cache(allow_output_mutation=True)
def get_cached_dataset(csv_file_path: str) -> pd.DataFrame:
    dataset = pd.read_csv(
        csv_file_path,
        dtype={'boundFrame': "Int64"}
    )
    return dataset

@st.cache()
def get_notna_index(dataset: pd.DataFrame) -> List[int]:
    return dataset.boundPixelPoint.isna().to_list()


st.set_page_config(layout="wide")
col1, col2 = st.columns([3, 1])

with col1:
    input_file_id = st.number_input("ファイル番号を入力", min_value=0, value=30, format='%d')
    input_file_id = int(input_file_id)
    csv_file_path = f"data/anns/original/csv/{str(input_file_id).zfill(4)}_ball.csv"
    input_frame_ids = get_input_frame_ids()

    dataset = get_cached_dataset(csv_file_path)

    output_file_path = st.text_input(
        label="csv出力するファイルパス",
        value=csv_file_path
    )
    output_button = st.button("csv出力")    

    frames = get_cached_images(input_file_id, input_frame_ids)
    for frame_id, frame in zip(input_frame_ids, frames):
        fig = px.imshow(frame)
        # [{'x': 551, 'y': 152, 'curveNumber': 0, 'pointNumber': [152, 551], 'pointIndex': [152, 551]}]
        selected_points = plotly_events(fig, override_height=600)
        if len(selected_points)>0:
            x = selected_points[0]['x']
            y = selected_points[0]['y']
            dataset.loc[dataset.boundFrame==frame_id, "boundPixelPoint"] = str([x, y])

with col2:
    indexes = get_notna_index(dataset)
    table = st.table(dataset[indexes][['boundFrame', 'boundPixelPoint']])    
    if output_button:
        dataset.to_csv(output_file_path, index=False)
        print("saved!!")
