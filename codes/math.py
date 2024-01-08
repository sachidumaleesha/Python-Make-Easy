import streamlit as st

def show_math():
    st.header("Math Operations")
    option = st.selectbox(
    'Select the example you want to see',
    ('Example-01', 'Example-02'))
   
    if option == 'Example-01':
        st.code('''
            import math

            a = float(input("Enter a:"))
            b = float(input("Enter b:"))
            c = math.sqrt(pow(a, 2) + pow(b, 2))
            print(f"c is: {c}")
            ''')
    elif option == 'Example-02':
        st.code('''    
            import math
                
            a = float(input("Enter value for side A: "))
            b = float(input("Enter value for side B: "))
            c = math.sqrt((a**2) + (b**2))
            print(f"The hypotenuse, or C, is equal to: {round(c, 2)}cm")
            ''')