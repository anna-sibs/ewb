import streamlit as st
import plotly.graph_objects as go

# Data
labels = ['Student Chapters', 'Professional Chapters']
values = [147, 57]
colors = ['#B36924', '#CBA052']

# Percentages for hover
total = sum(values)
percentages = [round(v / total * 100, 1) for v in values]
custom_hover = [f"{p}% {l}" for p, l in zip(percentages, labels)]

# Create donut chart
fig = go.Figure(go.Pie(
    labels=labels,
    values=values,
    hole=0.5,
    marker=dict(colors=colors),
    textinfo='label+value',
    textposition='outside',
    customdata=custom_hover,
    hovertemplate='%{customdata}<extra></extra>',
    outsidetextfont=dict(color='black', size=14),
    insidetextfont=dict(color='black', size=14)
))

# Layout
fig.update_layout(
    title="Distribution of Chapters in 2024",
    font=dict(family="Roboto, Arial, sans-serif", size=16),
    hoverlabel=dict(
        bgcolor="white",
        bordercolor="#B36924",
        font_size=18,
        font_family="Roboto, Arial, sans-serif"
    ),
    showlegend=False
)

# Streamlit render
st.title("EWB-USA Chapter Breakdown")
st.plotly_chart(fig, use_container_width=True)
