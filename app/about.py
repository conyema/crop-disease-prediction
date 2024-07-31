import streamlit as st


st.set_page_config(
    page_title="Crop Disease Diagnostics",
    page_icon=":material/potted_plant:",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Styling the header and subheaders
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        background: -webkit-linear-gradient(45deg, #09ab3b, #ffef00);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
        font-family: monospace, sans-serif;
        margin-bottom: 30px;
        border-bottom: 4px solid #162a3a; /* Secondary background color */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2); /* Soft text shadow */
    }
    .subheader {
        font-size: 26px;
        color: #0ded2e;
        margin-top: 25px;
        font-weight: bold;
        font-family: monospace, sans-serif;
        border-bottom: 2px solid #162a3a;; /* Secondary background color */
        padding-bottom: 5px;
    }
    .body-text {
        font-size: 20px;
        color: #333333; /* Dark text color for readability */
        font-family: monospace, sans-serif;
        line-height: 1.6; /* Improved line spacing */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Title
st.markdown('<p class="title">Crop Disease Diagnostics</p>', unsafe_allow_html=True)

# Introduction Subheader
st.markdown('<p class="subheader">Introduction</p>', unsafe_allow_html=True)

# Introduction Body
st.markdown(
    """
This project harnesses the power of advanced 
Convolutional Neural Networks (CNN) to assist farmers and agricultural experts in identifying and 
managing crop diseases and pest infestations, with a special focus on Urban Agriculture. 
"""
)

# Project Description and Our Work Subheader
st.markdown('<p class="subheader">Project Description </p>', unsafe_allow_html=True)

# Project Description and Our Work Body
st.markdown(
    """
Crop diseases and pest infestations pose significant challenges in agriculture, leading to reduced yields and financial losses. 
Early detection and diagnosis are crucial for effective management, especially in urban farming where space and resources are limited. 
The objective is to develop algorithms capable of recognizing early signs of pest infestations (such as changes in foliage/leaves and overall plant health)
and providing recommendations for combating them. This approach aims to minimize reliance on harmful chemical pesticides and promote sustainable,
eco-friendly pest control techniques, thereby reducing health risks associated with farming. Utilizing computer vision and fine-tuning pre-trained models
like ResNet and EfficientNet, I have built a comprehensive crop disease and infestation classification system for the following crops:
"""
)

# List of Crops
st.markdown(
    """
- **Apple**
- **Cucumber**
- **Potato**
- **Strawberry**
- **Tomato**
- **Lettuce**
- **Grapes**
- **Orange**
"""
)
