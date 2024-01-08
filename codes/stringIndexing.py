import streamlit as st

def show_stringIndexing():
    st.header("String Indexing")
    option = st.selectbox(
        'Select the exampleyou want to see',
        ('Example 01', 'Example 02')
    )

    if option == 'Example 01':
        st.code('''
            # indexing = accessing elements of a sequence 
            # using [] (indexing operator)
            # [start : end : step]
                
            # —---------------------
            #   EXAMPLE 1
            # —---------------------

            credit_number = "1234-5678-9012-3456"

            print(credit_number[0])
            print(credit_number[0:4])
            print(credit_number[:4])
            print(credit_number[4:8])
            print(credit_number[4:])
            print(credit_number[-1])
            print(credit_number[-4:])
            print(credit_number[::2])
            print(credit_number[::3])
        ''')
    if option == 'Example 02':
        st.code('''
            # indexing = accessing elements of a sequence 
            # using [] (indexing operator)
            # [start : end : step]
                
            # —---------------------
            #   EXAMPLE 2
            # —---------------------
                
            credit_number = "1234-5678-9012-3456"
            # last_digits = credit_number[-4:]
            # print(f"XXXX-XXXX-XXXX-{last_digits}")

            # EXERCISE 2
            credit_number = "1234-5678-9012-3456"
            credit_number = credit_number[::-1]
            print(credit_number)
        ''')