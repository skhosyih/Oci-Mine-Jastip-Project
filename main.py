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
packaging = 0

fullTransportFee = 40000
transportFee = fullTransportFee / 5

fullMealFee = 150000
mealFee = fullMealFee/ 5

# The form
with st.form("my_calculator"):
    st.subheader("Enter the Product Amount & Jastip Fee Percentage")
    myProductName = st.text_input("Product Name")
    myProductAmount = st.number_input('Product Amount')
    myJastipFeePercentage = st.number_input('Jastip Fee Percentage', min_value=0.1, max_value=0.3)
    submit = st.form_submit_button('Calculate!')
    
if submit:
    jastipFee = myJastipFeePercentage * myProductAmount
    st.write(f'The total is: Rp{myProductAmount + jastipFee + packaging + transportFee + mealFee:.2f}')
    st.write("Here's the detail")
    st.write()
    st.write("Product Name: ", myProductName)
    st.write(f'Product Amount: Rp{myProductAmount:.1f}')
    st.write("Product Amount: Rp", myProductAmount)
    st.write("Jastip Fee: Rp", jastipFee)
    st.write("Packaging: Rp", packaging)
    st.write("Transport Fee: Rp", transportFee)
    st.write("Meal Fee: Rp", mealFee)