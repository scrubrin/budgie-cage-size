import streamlit as st
import pandas as pd
import numpy as np

st.title('Budgie Cage Size Calculator')


st.write("This is for the cage that your budgies will spend most of their time in and call home. If the cage is smaller than recommended, you need to regularly let your birds out of the cage for many hours of the day, so they can fly as much as they want to for their physical and mental health.")

st.header("I have a cage in mind, would it suit?")
st.write("Please enter cage dimensions from the product description. Use internal measurements where possible. If the cage has a stand, exclude the stand height.")

#Define variables
cage_L = 45
cage_W = 45
cage_H = 45

# Initialize session state for the value if it doesn't exist
if "cage_L" not in st.session_state:
    st.session_state.cage_L = 45
if "cage_W" not in st.session_state:
    st.session_state.cage_W = 45
if "cage_H" not in st.session_state:
    st.session_state.cage_H = 45

# Callback function for when the slider changes
def update_number_input():
    st.session_state.num_input_L = st.session_state.slider_val_L
    st.session_state.num_input_W = st.session_state.slider_val_W
    st.session_state.num_input_H = st.session_state.slider_val_H

# Callback function for when the number input changes
def update_slider():
    st.session_state.slider_val_L = st.session_state.num_input_L
    st.session_state.slider_val_W = st.session_state.num_input_W
    st.session_state.slider_val_H = st.session_state.num_input_H

st.write("**Length (cm)**")

# Create the widgets, linking them via session state and callbacks
col1, col2 = st.columns(2)

with col1:
    st.slider(
        "Select Value with Slider",
        min_value=45,
        max_value=200,
        value=st.session_state.cage_L, # Initial value
        key="slider_val_L",               # Unique key for the slider
        on_change=update_number_input   # Callback when slider moves
    )

with col2:
    st.number_input(
        "Enter Value Manually",
        min_value=45,
        max_value=200,
        value=st.session_state.cage_L, # Initial value
        key="num_input_L",                # Unique key for the number input
        on_change=update_slider         # Callback when number input changes
    )

st.write("**Width (cm)**")
col3, col4 = st.columns(2)

with col3:
    st.slider(
        "Select Value with Slider",
        min_value=45,
        max_value=200,
        value=st.session_state.cage_W, # Initial value
        key="slider_val_W",               # Unique key for the slider
        on_change=update_number_input   # Callback when slider moves
    )

with col4:
    st.number_input(
        "Enter Value Manually",
        min_value=45,
        max_value=200,
        value=st.session_state.cage_W, # Initial value
        key="num_input_W",                # Unique key for the number input
        on_change=update_slider         # Callback when number input changes
    )

st.write("**Height (cm)**")
col5, col6 = st.columns(2)

with col5:
    st.slider(
        "Select Value with Slider",
        min_value=45,
        max_value=200,
        value=st.session_state.cage_H, # Initial value
        key="slider_val_H",               # Unique key for the slider
        on_change=update_number_input   # Callback when slider moves
    )

with col6:
    st.number_input(
        "Enter Value Manually",
        min_value=45,
        max_value=200,
        value=st.session_state.cage_H, # Initial value
        key="num_input_H",                # Unique key for the number input
        on_change=update_slider         # Callback when number input changes
    )

cage_L = st.session_state.num_input_L
cage_W = st.session_state.num_input_W
cage_H = st.session_state.num_input_H
BirdCheck= round(( cage_L * cage_W * cage_H ) / 90000)
st.write(f"**The number of birds this cage can house is {BirdCheck}.**")

st.write("Note that the bar spacing should be uniform and **not greater than 12mm.**")

st.write("Perches and feeders should be well-placed to maximise flying space within the cage.")