import streamlit as st
import datetime
import numpy as np


dico = {'with_mask': {datetime.date(2022, 4, 23): 991, datetime.date(2022, 4, 25): 241, datetime.date(2022, 4, 26): 1269, datetime.date(2022, 4, 24): 991}, 
'without_mask': {datetime.date(2022, 4, 23): 9, datetime.date(2022, 4, 25): 4, datetime.date(2022, 4, 26): 168, datetime.date(2022, 4, 24): 10}}


chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(dico)