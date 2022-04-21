import streamlit as st
from icu.services.simulation import Simul
import torch
import cv2

simu = Simul()

def app():
    
    ##########################
    ####     SIDEBAR      ####
    ##########################
    st.sidebar.write("---")
    select_mode = st.sidebar.radio("Choose a mode", ["Vidéo", "Simulation"])
    # info="Simulation : simulate detection and save it in db. \n Video : detect and display the detection on a video."
    st.sidebar.write("---")

    ##########################
    ####     Vidéo        ####
    ##########################
    if select_mode == "Vidéo":
        st.title("Vidéo")

        col1, mid, col2 = st.columns([20,1,20])


        if st.sidebar.button("Start"):
            stframe = st.empty()
            t = st.empty()
            # Chargement du model
            torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
            model = torch.hub.load("ultralytics/yolov5", "custom", path="icu/models/model_icu_20220404.pt")

            cap = cv2.VideoCapture("icu/datas/rue.mp4")
            # capture = st.video("icu/datas/rue.mp4")
            while cap.isOpened():
                ret, frame = cap.read()
                
                if not ret:
                    print("Can't receive frame (stream end?). Exiting ...")
                    exit()
                haut = frame.shape[0]
                large = frame.shape[1]
                # frame = cv2.resize(frame, (large//2, haut//2), interpolation=cv2.INTER_NEAREST)
                image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
                prediction =  model(image).pandas().xyxy[0].values

                if prediction is not None:
                    for pred in prediction:
                        print(pred)

                        x1 = int(pred[0])
                        y1 = int(pred[1])
                        x2 = int(pred[2])
                        y2 = int(pred[3])

                        start = (x1,y1)
                        end = (x2,y2)

                        name = pred[-1]
                        conf = pred[4]

                        if conf >= 0.3:
                            if name=="with_mask":
                                image = cv2.rectangle(image, start, end, (0,255,0))
                            elif name=="without_mask":
                                image = cv2.rectangle(image, start, end, (255,0,0))
                            else:
                                image = cv2.rectangle(image, start, end, (0,0,255))
                    
                stframe.image(image, use_column_width=True)
                # t.write(prediction)

        if st.sidebar.button("Stop"):
            cap.release()
            cv2.destroyAllWindows()

    ##########################
    ####   Simulation     ####
    ##########################
    if select_mode == "Simulation":
        st.title("Simulation")
        simu_duration = st.sidebar.text_input(label="duration", value="100")
        simu_sleep = st.sidebar.text_input(label="sleep", value="5")
        if st.sidebar.button("Launch"):
            Simul.auto_simul(duration=int(simu_duration), sleep=int(simu_sleep))
            # st.write("Simulation launched")
            # st.write("duration:", simu_duration)
            # st.write("sleep:", simu_sleep)


