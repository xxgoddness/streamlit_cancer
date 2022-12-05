import pickle
import numpy as np
import streamlit as st

#load save model 
model = pickle.load(open('lung_cancer.sav','rb'))

#judul web
st.text('191351020 | Dewi Nurmalasari - MalamC2019')
st.title('Prediksi Penyakit Kanker Paru - Paru')

col1, col2, col3 = st.columns (3)

with col1:
    GENDER = st.number_input('1 = Laki Laki , 2 = Perempuan ')
with col1:
    AGE = st.number_input('Umur')
with col1:
    SMOKING = st.number_input('SMOKING ? 1 = NO, 2 = YES')
with col1:
    YELLOW_FINGERS = st.number_input ('YELLOW FINGERS ? 1 = NO, 2 = YES')
with col1:
    ANXIETY = st.number_input('ANXIETY ?  1 = NO, 2 = YES')
with col2:
    PEER_PRESSURE = st.number_input ('PEER PRESSURE ? 1 = NO, 2 = YES')
with col2:
    CHRONIC_DISEASE = st.number_input ( 'CHRONIC_DISEASE ? 1 = NO, 2 = YES')
with col2:
    FATIGUE = st.number_input ('FATIGUE ? 1 = NO, 2 = YES')
with col2:
    ALLERGY = st.number_input ('ALLERGY ? 1 = NO, 2 = YES')
with col2:
    WHEEZING = st.number_input ('WHEEZING ? 1 = NO, 2 = YES')
with col3:
    ALCOHOL_CONSUMING = st.number_input ('ALCOHOL CONSUMING ? 1 = NO, 2 = YES')
with col3:
    COUGHING = st.number_input ('COUGHING ? 1 = NO, 2 = YES')
with col3:
    SHORTNESS_OF_BREATH = st.number_input ('SHORTNESS OF BREATH ? 1 = NO, 2 = YES')
with col3:
    SWALLOWING_DIFFICULTY = st.number_input ('SWALLOWING DIFFICULTY ? 1 = NO, 2 = YES')
with col3:
    CHEST_PAIN = st.number_input ('CHEST PAIN ? 1 = NO, 2 = YES')

#code prediction
cancer_diagnosis =''

#tombol
if st.button('Prediksi Penyakit Kanker Paru - Paru'):
    cancer_prediction = model.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE ,ALLERGY ,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])

    if (cancer_prediction [0]==1):
        cancer_diagnosis = 'Pasien Tidak Terkena Penyakit Kanker Paru - Paru'
    else:
        cancer_diagnosis = 'Pasien Terkena Penyakit Kanker Paru - Paru'

    st.success(cancer_diagnosis)
    
