import streamlit as st
from annotated_text import annotated_text

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
   st.subheader("Variable")
   option = st.selectbox(
    'Select the data type you want to see',
    ('Integer', 'Float', 'String', 'Boolean'))
   
   if option == 'Integer':
        st.code('''
            # variable = a reusable container for storing a 
            # value
            # a variable behaves as if it were the value it 
            # contains

            # INTEGER
            age = 21
            players = 2
            quantity = 5

            print(f"You are {age} years old")
            print(f"There are {players} players online")
            print(f"You would like to buy {quantity} items")
            ''')
   elif option == 'Float':
        st.code('''
            # variable = a reusable container for storing a 
            # value
            # a variable behaves as if it were the value it 
            # contains

            # FLOAT
            gpa = 3.2
            distance = 2.5
            price = 10.99

            print(f"Your gpa is {gpa}")
            print(f"You ran {distance}Km")
            print(f"The price is ${price}")
            ''')
   elif option == 'String':
        st.code('''
            # variable = a reusable container for storing a 
            # value
            # a variable behaves as if it were the value it 
            # contains

            # STRING
            name = "Bro"
            food = "pizza"
            email = "Bro123@gmail.com"

            print(f"Hello {name}")
            print(f"You like {food}")
            print(f"Your email is: {email}")
            ''')
   elif option == 'Boolean':
        st.code('''
            # variable = a reusable container for storing a 
            # value
            # a variable behaves as if it were the value it 
            # contains

            # BOOLEAN
            online = True
            for_sale = False
            running = False

            print(f"Are you online?: {online}")
            print(f"Is the item for sale?: {for_sale}")
            print(f"Game running: {running}")
            ''')

with col2:
   st.subheader("Typs Casting")
   st.code('''
        # type casting = The process of converting a value
        # of one data type to another
        # (string, integer, float, boolean)
        # Explicit vs Implicit

        name = "Bro"
        age = 21
        gpa = 1.9
        student = True

        # print(type(name))
        # print(type(age))
        # print(type(gpa))
        # print(type(student)) 

        age = float(age)
        print(age)

        gpa = int(gpa)
        print(gpa)

        student = str(student)
        print(student)

        name = bool(name)
        print(name)
        '''
    )

with col3:
   st.header("User Inputs")
   option = st.selectbox(
    'Select the example you want to see',
    ('Example-01', 'Example-02', 'Example-03'))
   
   if option == 'Example-01':
        st.code('''
            # ------------------------------------------------
            # EXERCISE 1 MAD LIBS
            # ------------------------------------------------
            adjective1 = input("Enter an adjective: ")
            noun = input("Enter a noun: ")
            adjective2 = input("Enter an adjective: ")
            verb = input("Enter a verb: ")
            adjective3 = input("Enter an adjective: ")

            print(f"Today I went to a {adjective1} zoo.")
            print(f"In an exhibit, I saw {noun}.")
            print(f"{noun} was {adjective2} and {verb}ing.")
            print(f"I was {adjective3}!")
            ''')
   elif option == 'Example-02':
        st.code('''
            # ------------------------------------------------
            # EXERCISE 2 AREA CALC
            # ------------------------------------------------
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))

            #area = length * width
            #print(f"The area is: {area}cm^2")
            ''')
   elif option == 'Example-03':
        st.code('''
            # ------------------------------------------------
            # EXERCISE 3 SHOPPING CART
            # ------------------------------------------------
            item = input("What item would you like to buy?: ")
            price = float(input("What is the price?: "))
            quantity = int(input("How many would you like?: "))

            total = price * quantity

            print(f"You have bought {quantity} x {item}/s")
            print(f"Your total is: ${round(total, 2)}")
            ''')

# Row-02
