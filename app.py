import streamlit as st
import requests
import datetime

'''
# TaxiFareModel front
'''
# Tittle of the app
st.title(' Taxi Fare Model')
st. subheader('Please, selecto ride parameters')

# Input from the user
pickup_date = st.date_input('Enter date', value=datetime.date.today())
pickup_time = st.time_input('Select the pickup time', value=datetime.datetime.now().time())
pickup_longitude = st.number_input('Pickup longitude')
pickup_latitude = st.number_input('Pickup latitude')
dropoff_longitude = st.number_input('Dropoff longitude')
dropoff_latitude = st.number_input('Dropoff latitude')
passenger_count = st.number_input('Enter passenger count', min_value=1, max_value = 8, value=1)


# Combine date and time to single datetime string
pickup_datetime = datetime.datetime.combine(pickup_date, pickup_time).strftime("%Y-%m-%d %H:%M:%S")

# Button to run prediction
if st.button('Get Fare'):
    ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
    #in a dictionary
    params = {
        'pickup_time': pickup_datetime,
        'pickup_longitude': pickup_longitude,
        'pickup_latitude': pickup_latitude,
        'dropoff_longitude': dropoff_longitude,
        'dropoff_latitude': dropoff_latitude,
        'passenger_count': passenger_count
    }


    ## Once we have these, let's call our API in order to retrieve a prediction
    url = 'https://taxifare.lewagon.ai/predict'
    #🤔 How could we call our API ? Off course... The `requests` package 💡
    #Let's call our API using the `requests` package...
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    # Let's retrieve the prediction from the **JSON** returned by the API...
    prediction = response.json

    ## Finally, we can display the prediction to the user
    st.subheader('Estimated Fare:')
    st.write(f"${prediction['fare']}")
