import streamlit as st

def show_whileLoop():
    st.header("While Loop")

    option = st.selectbox(
        'Select the example you want to see',
        ('Example-01', 'Example-02', 'Example-03', 'Example-04')
    )

    if option == 'Example-01':
        st.code('''
            # ---------------- EXAMPLE 1 ----------------

            name = input("Enter your name: ")

            while name == "":
                print("You did not enter your name!")
            name = input("Enter your name: ")

            print(f"Hello {name}")
        ''')
    elif option == 'Example-02':
        st.code('''
            # ---------------- EXAMPLE 2 ----------------

            age = int(input("Enter your age: "))

            while age < 0:
                print("Age can't be negative")
            age = int(input("Enter your age: "))

            print(f"You are {age} years old")
        ''')
    elif option == 'Example-03':
        st.code('''
            # ---------------- EXAMPLE 3 ----------------

            food = input("Enter a food you like (q to quit): ")

            while not food == "q":
                print(f"You like {food}")
            food = input("Enter another food you like (q to quit): ")

            print("bye")
        ''')
    elif option == 'Example-04':
        st.code('''
            # ---------------- EXAMPLE 4 ----------------

            num = int(input("Enter a # between 1 - 10: "))

            while num < 1 or num > 10:
                print(f"{num} is not valid")
                num = int(input("Enter a # between 1 - 10: "))

            print(f"You picked the number {num}")
        ''')