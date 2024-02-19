import streamlit as st
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

df = pd.read_csv("Cities1.csv")



list_variables = df.columns

st.title("Water and Air Pollution")

image_water = Image.open('water-update.jpg')
st.image(image_water, width=700)

# Display a header for the Visualization section
st.markdown("## Visualization")
symbols = st.multiselect("Select two variables", list_variables, ["City", "WaterPollution"])


tab1, tab2 = st.tabs(["Line Chart", "Bar Chart"])

tab1.subheader("Line Chart")
# Display a line chart for the selected variables
tab1.line_chart(data=df, x=symbols[0], y=symbols[1], width=0, height=0, use_container_width=True)

tab2.subheader("Bar Chart")
# Display a bar chart for the selected variables
tab2.bar_chart(data=df, x=symbols[0], y=symbols[1], use_container_width=True)






aq_min, aq_max = st.sidebar.slider('Select Air Quality Range', min_value=float(df['AirQuality'].min()), max_value=float(df['AirQuality'].max()), value=(float(df['AirQuality'].min()), float(df['AirQuality'].max())))
wp_min, wp_max = st.sidebar.slider('Select Water Pollution Range', min_value=float(df['WaterPollution'].min()), max_value=float(df['WaterPollution'].max()), value=(float(df['WaterPollution'].min()), float(df['WaterPollution'].max())))

# Filtering the dataframe based on the slider values
filtered_df = df[(df['AirQuality'] >= aq_min) & (df['AirQuality'] <= aq_max) & (df['WaterPollution'] >= wp_min) & (df['WaterPollution'] <= wp_max)]


tab3, tab4 = st.tabs(["Line Chart", "Bar Chart"])

tab3.subheader("Line Chart")
# Display a line chart for the selected variables
tab3.line_chart(data=filtered_df, x=symbols[0], y=symbols[1], width=0, height=0, use_container_width=True)

tab4.subheader("Bar Chart")
# Display a bar chart for the selected variables
tab4.bar_chart(data=filtered_df, x=symbols[0], y=symbols[1], use_container_width=True)




import streamlit.components.v1 as components


# Display the Sweetviz report
report_path = 'report.html'
HtmlFile = open(report_path, 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, height=1000,width=1000)





