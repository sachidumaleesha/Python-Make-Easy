import streamlit as st

def show_variable():
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