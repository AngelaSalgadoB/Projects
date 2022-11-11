import streamlit as st
value = st.slider('val') # this is a widget
st.write(value, 'squared is', value * value) 

import pandas as pd
st.title("Welcome to Streamlit!")
st.write("Our first DataFrame")
st.write( pd.DataFrame({ 'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8] }) )

checkbox_one = st.checkbox("Yes")
checkbox_two = st.checkbox("No")
if checkbox_one:
    value = "Yes"
elif checkbox_two:
    value = "No"
else:
    value = "No value selected"
st.write(f"You selected: {value}")

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")