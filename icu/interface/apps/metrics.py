import streamlit as st
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np
from datetime import datetime as dt
from icu.database.db_connect import Connexion

# Initiate instances
conn = Connexion()

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
    st.sidebar.write("---")

    ##########################
    ####      COUNT       ####
    ##########################

    count_duration = st.sidebar.expander(label="Display class count", expanded=False)
    
    A = count_duration.radio(" ", options=("All", "With mask", "Without mask"))
    if A == "With mask":
        value_mask = "with_mask"
    elif A == "Without mask":
        value_mask = "without_mask"
    elif A == "All":
        value_mask = "*"

    time_selected = count_duration.selectbox("Select the duration", options=list(duration_timestamp_choice.keys()), index=0)
    if time_selected != "<select file>":
        if count_duration.button("display"):
            st.write(f"you selected {time_selected}")
            for k,v in duration_timestamp_choice.items():
                if time_selected == k:
                    timestamp_value = v
            rep = conn.select_mask_period(value=value_mask, time=timestamp_value)

            
            for k,v in rep.items():
                st.write(f"{k} : {v}")


    ##########################
    ####      PLOT        ####
    ##########################

    if "select_date" not in st.session_state:
        st.session_state.select_date = {}


    ploting = st.sidebar.expander(label="Display plot", expanded=True)


    start_date = ploting.date_input("Start date")
    date1 = dt.strptime(str(start_date), "%Y-%m-%d")
    start_time = dt.timestamp(date1)

    end_date = ploting.date_input("End date")
    date2 = dt.strptime(str(end_date), "%Y-%m-%d")
    end_time = dt.timestamp(date2)

    col1, col2, col3 = ploting.columns(3)

    with col1:
        pie_button = st.button("Pie")
    # with col2:
    #     bar_button = st.button("Plotbar")
    # with col3:
    #     histo_button = st.button("Histo")

    val_pie = conn.select_dataviz(start_time, end_time)
    val_histo = conn.select_dataviz2(start_time, end_time)

    # Format values for count with/without
    data = []
    data_value_count = {}
    for row in val_pie:
        data.append(row[0])
    for i in set(data):
        data_value_count[i] = data.count(i)

    # Format values for histo day
    group_by_date = {x:{} for x in ["with_mask", "without_mask"]}
    select_drom_dates = {x:[] for x in ["with_mask", "without_mask"]}
    for i in val_histo:
        select_drom_dates[i[-1]].append(str(i[1]))

    for k, v in select_drom_dates.items():
        for i in set(v):
            group_by_date[k][i] = v.count(i)

    """
    {'with_mask': {datetime.date(2022, 3, 4): 991, datetime.date(2022, 4, 22): 241, datetime.date(2022, 4, 26): 1269, datetime.date(2022, 2, 24): 991}, 
    'without_mask': {datetime.date(2022, 3, 4): 9, datetime.date(2022, 4, 22): 4, datetime.date(2022, 4, 26): 168, datetime.date(2022, 2, 24): 10}}

    """



    # Pie

    labels = []
    values = []
    for k, v in data_value_count.items():
        labels.append(k)
        values.append(v)

    st.markdown(f"<h1 style='text-align: center;'>Période du {date1.strftime('%d-%m')} au {date2.strftime('%d-%m')}</h1>", unsafe_allow_html=True)
    st.write("---")

    if pie_button:
        with st.container():
            col1, mid, col2 = st.columns([20,1,20])
            if values:
                with col1:
                    fig1, ax1 = plt.subplots(figsize=(2, 2))
                    ax1.pie(values, labels=labels, autopct="%1.1f%%", shadow=True, startangle=90)
                    ax1.axis('equal')
                    st.pyplot(fig1)
                with col2:
                    with st.container():
                        st.markdown("<h1 style='height:4em;'><h1>", unsafe_allow_html=True)

                    with st.container():
                        for k, v in data_value_count.items():
                            st.markdown(f"<h2>{k} : <span style='color:red'>{v}</span></h2>", unsafe_allow_html=True)

            else:
                st.write("There is no datas to display")

        st.write("---")
        print(group_by_date)
        st.bar_chart(data=group_by_date)
        st.area_chart(data=group_by_date)
        # with st.container():
        #     fig = ff.create_distplot(values, labels, bin_size=[.1, .25, .5])

        #     st.plotly_chart(fig, use_container_width=True)






