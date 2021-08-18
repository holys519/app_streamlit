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

    local_image = open(local_image_path, "rb")


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


import streamlit as streamlit
st.title('物体検出アプリ')

uploaded_file = st.file_uploader ('choose as image...', type=['jpg', 'png'])
if uploaded_file is not None:
    Image.open(uploaded_file)
    img_path = f'img/{upload_file.name}'
    img.save(img_path)
    st.image(img)





    st.markdown('**認識されたコンテンツタグ**')
    st.markdown('> apple, tree, building, green')