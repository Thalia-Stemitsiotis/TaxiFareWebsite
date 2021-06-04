import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np
#from geopy.geocoders import Nominatim

'''
# NY Taxi Prediction App
'''

d = st.date_input(
    "Enter date: yyyy/mm/dd")

t = st.time_input('Time:')

pickup_location = st.text_input('Enter your pickup adress here', '')
dropoff_location = st.text_input('Enter your dropoff adress here', '')

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

map_data = pd.DataFrame(
    columns=['lat', 'lon'])
st.map(map_data)

if st.button('Click here for taxi fare price'):
    response = requests.get(url, params).json()
    price = round(response['prediction'], 2)
    st.success(f'Predicted taxi fare price: {price}')