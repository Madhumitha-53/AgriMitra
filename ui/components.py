import streamlit as st



def info_card(icon, title, value):
    """Render a styled info card."""
    st.markdown(
        f"""
<div class="card">
  <div class="dashboard-icon">{icon}</div>
  <div class="dashboard-title">{title}</div>
  <div class="dashboard-value">{value}</div>
</div>
""",
        unsafe_allow_html=True,
    )



def section_header(text):
    """Render a section header with consistent styling."""
    st.markdown(
        f'<h2 style="color:inherit;">{text}</h2>',
        unsafe_allow_html=True,
    )
