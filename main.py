from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

subscription_key = "c7f333fe6f0e465095487b8c71600380"
endpoint = "https://202108yama.cognitiveservices.azure.com/"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

def get_tags(filepath):

    local_image = open(filepath, "rb")


    tags_result = computervision_client.tag_image_in_stream(local_image)
    tags = tags_result.tags
    tags_name = []
    for tag in tags:
        tags_name.append(tag.name)

    return tags_name

def detect_objects(filepath):

    local_image = open(filepath, "rb")

    detect_objects_results = computervision_client.detect_objects_in_stream(local_image)
    objects = detect_objects_results.objects
    return objects


import streamlit as st
from PIL import ImageDraw
from PIL import ImageFont
st.title('物体検出アプリ')
st.text('物体')

uploaded_file = st.file_uploader ('choose as image...', type=['jpg', 'png'])
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img_path = f'img/{uploaded_file.name}'
    img.save(img_path)
    objects = detect_objects(img_path)
    # 描画
    draw = ImageDraw.Draw(img)
    for object in objects:
        x = object.rectangle.x
        y = object.rectangle.y
        w = object.rectangle.w
        h = object.rectangle.h
        caption = object.object_property

        font = ImageFont.truetype(font='./Helvetica 400.ttf', size=50)
        text_w, text_h = draw.textsize(caption, font=font)

        draw.rectangle([(x, y),(x+w, y+h)], fill=None, outline='green', width=5)
        draw.rectangle([(x, y),(x+text_w, y+text_h)], fill='green', outline='green')
        draw.text((x,y), caption, fill='white', font=font)


    st.image(img)

    tags_name = get_tags(img_path)
    tags_name = ','.join(tags_name)
    st.markdown('**認識されたコンテンツタグ**')
    st.markdown(f'> {tags_name}')

import streamlit as st
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="example")
# import numpy as np
# def main():
#     selected_box = st.sidebar.selectbox(
#         'Choose one of the following',
#         ('Welcome','Image Processing', 'Video', 'Face Detection', 'Feature Detection', 'Object Detection')
#         )
#     if selected_box == 'Welcome':
#             welcome() 
#     if selected_box == 'Image Processing':
#             photo()
#     if selected_box == 'Video':
#             video()
#     if selected_box == 'Face Detection':
#             face_detection()
#     if selected_box == 'Feature Detection':
#             feature_detection()
#     if selected_box == 'Object Detection':
#             object_detection()
# if __name__ == "__main__":
#     main()

