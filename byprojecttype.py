import streamlit as st

import plotly.graph_objects as go

# Data
non_water_data = {
    'Agriculture': 24,
    'Civil Works': 26,
    'Energy': 16,
    'Sanitation': 38,
    'Structures': 46
}
bar_colors = ['#B36924', '#4E3524', '#8A8D4A', '#CBA052', '#3D3935']

fig = go.Figure(go.Bar(
    x=list(non_water_data.keys()),
    y=list(non_water_data.values()),
    marker=dict(
        color=bar_colors,
        line=dict(width=0, color='rgba(0,0,0,0)')
    ),
    width=0.4,
    hovertemplate='%{x}: %{y}<extra></extra>'
))

fig.update_layout(
    title="Breakout of Other Infrastructure Projects (2024)",
    title_font=dict(size=24),
    font=dict(size=16),
    showlegend=False,
    bargap=0.5,
    plot_bgcolor='#ABCAE9',
    paper_bgcolor='white',
    hoverlabel=dict(
        bgcolor='white',
        bordercolor='#B36924',
        font_size=18,
        font_family='Arial'
    )
)

fig.update_xaxes(tickangle=0)
st.plotly_chart(fig, use_container_width=True)
