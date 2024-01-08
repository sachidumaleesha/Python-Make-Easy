import streamlit as st
from codes.variable import show_variable
from codes.typeCasting import show_typeCasting
from codes.userInputs import show_userInputs
from codes.math import show_math
from codes.ifelse import show_ifelse

st.set_page_config(page_title='Python Make Easy - Streamlit', layout = 'wide', page_icon = 'python.svg', initial_sidebar_state = 'expanded')

with st.sidebar:
    st.image('streamlit.svg', width=40)
    st.write('Powerd by Streamlit')

    st.subheader('Download Python')
    link_to_python = "https://www.python.org/downloads"
    st.code(link_to_python)

    st.subheader('Downlaod VsCode or Pychrm')
    link_to_vscode = "https://code.visualstudio.com"
    st.code(link_to_vscode)
    link_to_pycharm = "https://www.jetbrains.com/pycharm"
    st.code(link_to_pycharm)

    st.subheader('Code to run Python File')
    code = 'python filename.py'
    st.code(code)


st.header('Python Make Easy For You')
col1, col2, col3 = st.columns(3)

# Row-01
with col1:
   show_variable()
   show_math()

with col2:
   show_typeCasting()
   show_ifelse()

with col3:
   show_userInputs()