import streamlit as st
from datetime import datetime as dt
from icu.database.db_connect import Connexion

# Initiate instances
conn = Connexion()

def value_selector(dico):

    # Add a string in choice when you load page
    option = st.sidebar.selectbox("Select the duration", options=list(dico.keys()), index=0)

    return option

def app():

    duration_timestamp_choice = {
        "<select file>": None,
        "15 min": 900,
        "30 min": 1800,
        "1h": 3600,
        "6h": 21600,
        "12h": 43200,
        "24h": 86400,
        "1 week": 604800,
        "1 month": 2419200,
        "all": round(dt.now().timestamp()) 
        }
    A = st.sidebar.radio(" ", options=("All", "With mask", "Without mask"))


    if A == "With mask":
        value_mask = "with_mask"
    elif A == "Without mask":
        value_mask = "without_mask"
    elif A == "All":
        value_mask = "*"
    st.sidebar.write("---")

    time_selected = value_selector(duration_timestamp_choice)
    if time_selected != "<select file>":
        if st.sidebar.button("display"):
            st.write(f"you selected {time_selected}")
            for k,v in duration_timestamp_choice.items():
                if time_selected == k:
                    timestamp_value = v
            rep = conn.select_mask_period(value=value_mask, time=timestamp_value)

            
            for k,v in rep.items():
                st.write(f"{k} : {v}")
