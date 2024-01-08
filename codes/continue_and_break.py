import streamlit as st

def show_continue_and_break():
    st.header("Continue and Break")
    option = st.selectbox(
        'Select Continue or Break',
        ('Continue', 'Break')
    )

    if option == 'Continue':
        st.code('''
            # ---------------- CONTINUE ----------------

            for x in range(1, 21):
            if x == 13:
                continue
            else:
                print(x)
        ''')
    elif option == 'Break':
        st.code('''
            # ---------------- BREAK ----------------

            for x in range(1, 21):
            if x == 13:
                break
            else:
                print(x)
        ''')