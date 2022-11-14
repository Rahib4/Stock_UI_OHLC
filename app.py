import pandas as pd
import streamlit as st
from draw_candlestick_complex import get_candlestick_plot

st.set_page_config(layout="wide")

# Sidebar options
ticker = st.sidebar.selectbox(
    'Ticker to Plot',   
    options = ['TSLA', 'MSFT', 'AAPL']
)

days_to_plot = st.sidebar.slider(
    'Days to Plot', 
    min_value = 1,
    max_value = 300,
    value = 120,
)
ma1 = st.sidebar.number_input(
    'Moving Average #1 Length',
    value = 10,
    min_value = 1,
    max_value = 120,
    step = 1,    
)
ma2 = st.sidebar.number_input(
    'Moving Average #2 Length',
    value = 20,
    min_value = 1,
    max_value = 120,
    step = 1,    
)

# Get the dataframe and add the moving averages
df = pd.read_csv(f'{ticker}.csv')
df[f'{ma1}_ma'] = df['Close'].rolling(ma1).mean()
df[f'{ma2}_ma'] = df['Close'].rolling(ma2).mean()
df = df[-days_to_plot:]

# Display the plotly chart on the dashboard

# layout = go.Layout(
#     autosize=False,
#     width=1000,
#     height=1000,

#     xaxis= go.layout.XAxis(linecolor = 'black',
#                           linewidth = 1,
#                           mirror = True),

#     yaxis= go.layout.YAxis(linecolor = 'black',
#                           linewidth = 1,
#                           mirror = True),

#     margin=go.layout.Margin(
#         l=50,
#         r=50,
#         b=100,
#         t=100,
#         pad = 4
#     )
# )

# st.update_layout(height=800)
fig = get_candlestick_plot(df, ma1, ma2, ticker)
fig.update_layout(title_text="Stock Candlestick Chart", margin={"r": 0, "t": 0, "l": 0, "b": 0}, height=800)
st.plotly_chart(
    fig,
    use_container_width = True
    # height=1800
)

#nativefier --name Stock_Ticker_App http://192.168.1.5:8501 --platform "windows"