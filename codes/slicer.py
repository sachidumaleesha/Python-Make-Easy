import streamlit as st

def show_slicer():
    st.header("Slicer")
    st.code('''
        email = input("Enter your email: ")

        username = email[:email.index("@")]
        domain = email[email.index("@") + 1:]

        print(f"Your username is {username} and domain is {domain}")
    ''')