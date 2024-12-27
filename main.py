# Run it with 'streamlit run main.py

# Import streamlit
import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Oci & Mine's Jastip Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded")

# Initialize the Streamlit app
st.title("Oci & Mine's Jastip Calculator")
st.write("An interesting entrusted service project initiated by two people, Oci and Mine, that can calculate the entire price of the product along with the 'jastip' rate, transportation costs, packaging, and meal costs, with a fair price")

# Enter the initial price product amount and initial other variables
priceProduct = 0

percentageJastipFee = 0.1

packaging = 0

fullTransportFee = 40000
transportFee = fullTransportFee / 5

fullMealFee = 150000
mealFee = fullMealFee/ 5

# The form
with st.form("my_calculator"):
    st.title("## Enter the Product Amount")
    myProductAmount = st.number_input('myProductAmount')
    submit = st.form_submit_button('Calculate!')
    
if submit:
    jastipFee = percentageJastipFee * priceProduct
    st.write(f'{myProductAmount + jastipFee + transportFee + mealFee:.2f}')
    st.write("Here's the detail")
    st.write()
    st.write("Price Product: ", priceProduct)
    st.write("Jastip Fee: ", jastipFee)
    st.write("Packaging: ", packaging)
    st.write("Transport Fee: ", transportFee)
    st.write("Meal Fee: ", mealFee)