import streamlit as st
import plotly.graph_objects as go

# --- Data for first two charts ---
water_projects = 207
non_water_total = 150
non_water_data = {
    'Agriculture': 24,
    'Civil Works': 26,
    'Energy': 16,
    'Sanitation': 38,
    'Structures': 46
}
bar_colors = ['#B36924', '#4E3524', '#8A8D4A', '#CBA052', '#3D3935']

# --- Data for third chart (Chapters Donut) ---
chapter_labels = ['Student Chapters', 'Professional Chapters']
chapter_values = [147, 57]
chapter_colors = ['#B36924', '#CBA052']
chapter_total = sum(chapter_values)
chapter_percentages = [round(v / chapter_total * 100, 1) for v in chapter_values]
chapter_hover = [f"{p}% {l}" for p, l in zip(chapter_percentages, chapter_labels)]

# --- Layout: Title
st.title("Other Types of Active Infrastructure Projects 2024")

# --- Column layout with extra space for center chart
col1, col2, col3 = st.columns([1, 1.6, 1])

# --- Donut chart (left) ---
with col1:
    fig1 = go.Figure(go.Pie(
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

    fig1.update_layout(
        title="Water vs Other Infrastructure",
        font=dict(size=16, family="Roboto, Arial, sans-serif"),
        hoverlabel=dict(
            bgcolor='white',
            bordercolor='#B36924',
            font_size=18,
            font_family='Roboto, Arial, sans-serif'
        ),
        showlegend=False
    )

    st.plotly_chart(fig1, use_container_width=True)

# --- Bar chart (center) ---
with col2:
    fig2 = go.Figure(go.Bar(
        x=list(non_water_data.keys()),
        y=list(non_water_data.values()),
        marker=dict(color=bar_colors, line=dict(width=0, color='rgba(0,0,0,0)')),
        width=0.4,
        hovertemplate='%{x}: %{y}<extra></extra>'
    ))

    fig2.update_layout(
        title="Breakout of Other Infrastructure Projects",
        font=dict(size=16, family="Roboto, Arial, sans-serif"),
        showlegend=False,
        bargap=0.5,
        plot_bgcolor='#ABCAE9',
        paper_bgcolor='white',
        hoverlabel=dict(
            bgcolor='white',
            bordercolor='#B36924',
            font_size=18,
            font_family='Roboto, Arial, sans-serif'
        )
    )

    fig2.update_xaxes(tickangle=0)

    st.plotly_chart(fig2, use_container_width=True)

# --- Chapters donut (right) ---
with col3:
    fig3 = go.Figure(go.Pie(
        labels=chapter_labels,
        values=chapter_values,
        hole=0.5,
        marker=dict(colors=chapter_colors),
        textinfo='label+value',
        textposition='outside',
        customdata=chapter_hover,
        hovertemplate='%{customdata}<extra></extra>',
        outsidetextfont=dict(color='black', size=14),
        insidetextfont=dict(color='black', size=14)
    ))

    fig3.update_layout(
        title="Distribution of Chapters in 2024",
        font=dict(size=16, family="Roboto, Arial, sans-serif"),
        hoverlabel=dict(
            bgcolor="white",
            bordercolor="#B36924",
            font_size=18,
            font_family="Roboto, Arial, sans-serif"
        ),
        showlegend=False
    )

    st.plotly_chart(fig3, use_container_width=True)
