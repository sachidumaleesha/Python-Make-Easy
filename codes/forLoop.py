import streamlit as st

def show_forloop():
    st.header("For Loop")
    option = st.selectbox(
        'Select the example you want to see',
        ('Example-01 ', 'Example-02 ', 'Example-03 ', 'Example-04 ')
    )

    if option == 'Example-01 ':
        st.code('''
            # for loops = execute a block of code a fixed number of times.
            # You can iterate over a range, string, sequence, etc.

            # ---------------- EXAMPLE 1 ----------------

            for x in range(1, 11):
                print(x)
        ''')
    elif option == 'Example-02 ':
        st.code('''
            # for loops = execute a block of code a fixed number of times.
            # You can iterate over a range, string, sequence, etc.
                
            # ---------------- EXAMPLE 2 ----------------

            for x in reversed(range(1, 11)):
                print(x)

            print("Happy New Year!")
        ''')
    elif option == 'Example-03 ':
        st.code('''
            # for loops = execute a block of code a fixed number of times.
            # You can iterate over a range, string, sequence, etc.
                
            # ---------------- EXAMPLE 3 ----------------

            for x in range(1, 11, 2):
            print(x)
        ''')
    elif option == 'Example-04 ':
        st.code('''
            # for loops = execute a block of code a fixed number of times.
            # You can iterate over a range, string, sequence, etc.
                
            # ---------------- EXAMPLE 4 ----------------

            credit_card = "1234-5678-9012-3456"

            for x in credit_card:
                print(x)
        ''')
        