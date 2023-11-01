import streamlit as st
import pandas as pd
import plotly.graph_objs as go

# Load data from the Excel file
excel_file = pd.ExcelFile('testdata.xlsx')

# Create a list of worksheet names
worksheet_names = excel_file.sheet_names

# Title and introduction
st.title("0.8V Carbon run")
st.write("Select two worksheets from 'testdata.xlsx' to display the data plots.")

# Dropdown to select the first worksheet
selected_worksheet1 = st.selectbox("Select the first worksheet:", worksheet_names)

# Dropdown to select the second worksheet
selected_worksheet2 = st.selectbox("Select the second worksheet:", worksheet_names)

# Load data from the selected worksheets
df1 = excel_file.parse(selected_worksheet1, header=None)
x_data1 = df1.iloc[:, 0]
y_data1 = df1.iloc[:, 1]

df2 = excel_file.parse(selected_worksheet2, header=None)
x_data2 = df2.iloc[:, 0]
y_data2 = df2.iloc[:, 1]

# Radio button to select plot mode for the first worksheet
plot_mode1 = st.radio("Select plot mode for the first worksheet:", ["Markers", "Lines+Markers", "Lines"])

fig1 = go.Figure()

fig1.update_layout(width=800, height=400)

fig1.update_layout(xaxis_title="Time(sec)", yaxis_title="Current(nA)")

# Add grid lines
fig1.update_layout(xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
                   yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'))

if plot_mode1 == "Markers":
    fig1.add_trace(go.Scatter(x=x_data1, y=y_data1, mode='markers', marker=dict(size=2), name='markers'))
elif plot_mode1 == "Lines+Markers":
    fig1.add_trace(go.Scatter(x=x_data1, y=y_data1, mode='lines+markers', line=dict(width=1, color='blue'), marker=dict(size=4, color='red'), name='lines+markers'))
elif plot_mode1 == "Lines":
    fig1.add_trace(go.Scatter(x=x_data1, y=y_data1, mode='lines', name='lines'))

# Checkbox to control rolling average visibility for the first worksheet
show_rolling_average1 = st.checkbox("Show Rolling Average for the first worksheet")

if show_rolling_average1:
    rolling_window1 = st.slider("Rolling Average Window (1st worksheet)", min_value=1, max_value=100, value=5)
    rolling_average1 = y_data1.rolling(rolling_window1).mean()
    fig1.add_trace(go.Scatter(x=x_data1, y=rolling_average1, mode='lines', name=f'Rolling Average (Window {rolling_window1})', line=dict(color='green')))

# Radio button to select plot mode for the second worksheet
plot_mode2 = st.radio("Select plot mode for the second worksheet:", ["Markers", "Lines+Markers", "Lines"])

fig2 = go.Figure()

fig2.update_layout(width=800, height=400)

fig2.update_layout(xaxis_title="Time(sec)", yaxis_title="Current(nA)")

# Add grid lines for the second worksheet
fig2.update_layout(xaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'),
                   yaxis=dict(showgrid=True, gridwidth=1, gridcolor='lightgray'))

if plot_mode2 == "Markers":
    fig2.add_trace(go.Scatter(x=x_data2, y=y_data2, mode='markers', marker=dict(size=2), name='markers'))
elif plot_mode2 == "Lines+Markers":
    fig2.add_trace(go.Scatter(x=x_data2, y=y_data2, mode='lines+markers', line=dict(width=1, color='blue'), marker=dict(size=4, color='red'), name='lines+markers'))
elif plot_mode2 == "Lines":
    fig2.add_trace(go.Scatter(x=x_data2, y=y_data2, mode='lines', name='lines'))

# Checkbox to control rolling average visibility for the second worksheet
show_rolling_average2 = st.checkbox("Show Rolling Average for the second worksheet")

if show_rolling_average2:
    rolling_window2 = st.slider("Rolling Average Window (2nd worksheet)", min_value=1, max_value=100, value=5)
    rolling_average2 = y_data2.rolling(rolling_window2).mean()
    fig2.add_trace(go.Scatter(x=x_data2, y=rolling_average2, mode='lines', name=f'Rolling Average (Window {rolling_window2})', line=dict(color='green')))

# Display the figures
st.plotly_chart(fig1)
st.plotly_chart(fig2)
