import streamlit as st
import datetime
import requests


'''
# NY Taxi Prediction App
'''

d = st.date_input(
    "Enter date: yyyy/mm/dd")

t = st.time_input('Time:')
p_longitude = st.number_input('Pickup longitude')
p_latitude = st.number_input('Pickup latitude')
d_longitude = st.number_input('Dropoff longitude')
d_latitude = st.number_input('Dropoff latitude')
p_count = st.number_input('Passenger count')

date_time = str(datetime.datetime.combine(d, t))

url = 'https://taxifare.lewagon.ai/predict'
params = {
    'pickup_datetime': date_time,
    'pickup_longitude':p_longitude,
    'pickup_latitude':p_latitude,
    'dropoff_longitude':d_longitude,
    'dropoff_latitude':d_latitude,
    'passenger_count':int(p_count)}

if st.button('Click here for taxi fare price'):
    response = requests.get(url, params).json()
    price = round(response['prediction'], 2)
    st.success(f'Predicted taxi fare price: {price}')