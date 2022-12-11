# To run use
# $ streamlit run yolor_streamlit_demo.py
#from yolor import *
from yolo_v7 import *
import tempfile
import cv2
import torch

from utils.hubconf import custom
from utils.plots import plot_one_box

from models.models import *
from utils.datasets import *
from utils.general import *

import streamlit as st
from PIL import ImageColor

def main():
    
    st.title("Car Detection Dashboard YOLOV7 | Pyresearch")
    st.sidebar.title('Set')

    # 
    st.sidebar.markdown('---')

    # path to model
    path_model_file = st.sidebar.text_input(
    'Yolov7 model path',
    'yolov7.pt'
    )

     #
    st.sidebar.markdown('---')

    # Class txt
    path_to_class_txt = st.sidebar.file_uploader(
    'class file:', type=['txt']
    )
    #
    st.sidebar.markdown('---')

    if path_to_class_txt is not None:

        options = st.sidebar.radio(
            'Select:', ('Webcam', 'Image', 'Video', 'RTSP'), index=1)

        gpu_option = st.sidebar.radio(
            'Select:', ('CPU', 'GPU'))
        if not torch.cuda.is_available():
            st.sidebar.warning('CUDA Not Available, So choose CPU', icon="⚠️")
        else:
            st.sidebar.success(
                'GPU is Available on this Device, Choose GPU for the best performance',
                icon="✅"
            )
        st.sidebar.markdown('---')

        # Confidence
        confidence = st.sidebar.slider(
            'Detection Confidence', min_value=0.0, max_value=1.0, value=0.25)

        # Draw thickness
        draw_thick = st.sidebar.slider(
            'Draw Thickness:', min_value=1,
            max_value=20, value=3
        )

        st.sidebar.markdown('---')






if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass