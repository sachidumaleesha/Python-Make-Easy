import streamlit as st

def show_stringMethods():
    st.header("String Methods")
    option = st.selectbox(
        'Select the example you want to see',
        ('Example 01', 'Example 02')
    )

    if option == 'Example 01':
        st.code('''
            # -------------------------------
            # Example 1
            # -------------------------------
            name = input("Enter your name: ")
            phone_number = input("Enter your phone #: ")

            length = len(name)
            index = name.find(" ")
                
            name1 = name.capitalize()
            name2 = name.upper()
            name3 = name.lower()
                
            result1 = name.isdigit()
            result2 = name.isalpha()
            result3 = phone_number.count(" ")
                
            phone_number = phone_number.replace("-", "")
        ''')
    elif option == 'Example 02':
        st.code('''
            # -------------------------------
            # Example 2
            # -------------------------------
            username = input("Enter a username: ")

            if len(username) > 12:
                print("Your name can't be more than 12 characters")
            elif not username.find(" ") == -1:
                print("Your username can't contain spaces")
            elif not username.isalpha():
                print("Your username can't contain digits")
            else:
                print(f"Welcome {username}!")
        ''')