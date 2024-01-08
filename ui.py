import streamlit as st
from codes.variable import show_variable
from codes.typeCasting import show_typeCasting
from codes.userInputs import show_userInputs
from codes.math import show_math
from codes.ifelse import show_ifelse
from codes.logicalOperators import show_logicalOperators
from codes.stringMethods import show_stringMethods
from codes.stringIndexing import show_stringIndexing
from codes.slicer import show_slicer
from codes.formatSpecifiers import show_formatSpecifiers
from codes.whileLoop import show_whileLoop
from codes.forLoop import show_forloop
from codes.continue_and_break import show_continue_and_break
from codes.nestedLoop import show_nestedLoop

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

    st.subheader('Code to run normal Python File')
    code = 'python filename.py'
    st.code(code)

    st.subheader('Code to run Stremlit Python File')
    streamlit = 'streamlit run filename.py'
    st.code(streamlit)


st.header('Python Make Easy For You')
col1, col2, col3 = st.columns(3)

# Row-01
with col1:
   show_variable()
   show_math()
   show_stringMethods()
   show_formatSpecifiers()
   show_continue_and_break()

with col2:
   show_typeCasting()
   show_ifelse()
   show_stringIndexing()
   show_whileLoop()
   show_nestedLoop()

with col3:
   show_userInputs()
   show_logicalOperators()
   show_slicer()
   show_forloop()