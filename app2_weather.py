import streamlit as st
import pandas as pd
import plost
import base64

st.set_page_config(layout='wide', initial_sidebar_state='expanded')


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Weatherboard `version 1.0.1`')

st.sidebar.subheader('Thermal map parameter')
time_hist_color = st.sidebar.selectbox('`Color by`', ('tmin', 'tmax')) 

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('`Select data`', ('q1', 'q2'))

st.sidebar.subheader('pollution chart parameters')
plot_data = st.sidebar.multiselect('`Select data`', ['tmin', 'tmax'], ['tmin', 'tmax'])
plot_height = st.sidebar.slider('`Specify plot height`', 200, 500, 250)

st.sidebar.markdown('''
---
`Created with ❤️ by `[dinesh](https://github.com/dinesh26112002/).
''')

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)


# Row A
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Row B
seattle_weather = pd.read_csv('chennai_weather.csv', parse_dates=['date'])
stocks = pd.read_csv('foo.csv')

c1, c2 = st.columns((5,5))
with c1:
    st.markdown('### Thermalmap(days,week)')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color=time_hist_color,
    aggregate='median',
    legend=None,
    height=345,
    use_container_width=True)
with c2:
    st.markdown('### Donut chart(area)')
    plost.donut_chart(
        data=stocks,
        theta=donut_theta,
        color='city',
        legend='bottom', 
        use_container_width=True)

# Row C
st.markdown('### Pollution chart(1990-2022)')
st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('pollution.jpg')    