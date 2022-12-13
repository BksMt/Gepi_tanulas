import streamlit as st

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import pickle

if __name__ == '__main__':
  prec = st.number_input('Precipitation)
  min= st.number_input('Min temp)
  wind= st.number_input('Wind)
  weather= st.number_input('Weather)
