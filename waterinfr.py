import plotly.graph_objects as go

# Data
water_projects = 207
non_water_total = 150

fig = go.Figure(go.Pie(
    labels=["Water Projects", "Other<br>Infrastructure"],
    values=[water_projects, non_water_total],
    hole=0.5,
    marker_colors=["#0065b2", "#ABCAE9"],
    textinfo='label+percent',
    textposition='outside',
    hoverinfo='label+percent',
    rotation=160,
    outsidetextfont=dict(color='black', size=14),
    insidetextfont=dict(color='black', size=14)
))

fig.update_layout(
    title="Water vs Other Infrastructure Projects in 2024",
    title_font=dict(size=24),
    hoverlabel=dict(
        bgcolor='white',
        bordercolor='#B36924',
        font_size=18,
        font_family='Arial'
    ),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)  # ✅ this will work
