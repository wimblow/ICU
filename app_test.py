import streamlit as st
from datetime import date
import numpy as np
import pandas as pd



dico = {'with_mask': {"2022, 4, 23": 991, "2022, 4, 25": 241, "2022, 4, 26": 1269, "2022, 4, 24": 991}, 
'without_mask': {"2022, 4, 23": 9, "2022, 4, 25": 4, "2022, 4, 26": 168, "2022, 4, 24": 10}}

st.bar_chart(data=dico)
st.area_chart(data=dico)