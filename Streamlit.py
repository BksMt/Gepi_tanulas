import streamlit as st

import numpy as np
import pandas as pd
import pickle

load_model = pickle.load(open('linear_model.sav', 'rb'))
load_scaler = pickle.load(open('scaler.pkl', 'rb'))

def weather_prediction(imput_data):
  imput_data = load_scaler.transform(imput_data)
  prediction = load_model.predict(imput_data)
  return prediction

if __name__ == '__main__':
  prec = st.number_input('Precipitation')
  min = st.number_input('Min temp')
  wind= st.number_input('Wind')
  weather= st.number_input('Weather')
  prediction = weather_prediction([[prec, min, wind, weather]])
  if st.button('Predict'):
    st.success(prediction)
