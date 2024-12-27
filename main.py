# Run it with 'streamlit run main.py'

# Import streamlit
import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Oci & Mine's Jastip Calculator",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize the Streamlit app
st.title("Oci & Mine's Jastip Calculator")
st.write("An interesting entrusted service project initiated by two people, Oci and Mine, that can calculate the entire price of the product along with the 'jastip' rate, transportation costs, packaging, and meal costs, with a fair price")

# Enter the initial price product amount and initial other variables
priceProduct = 0
packaging = 0

fullTransportFee = 40000
transportFee = fullTransportFee / 5

fullMealFee = 150000
mealFee = fullMealFee / 5

# Function to format numbers as Rupiah
def format_rupiah(value):
    return f"Rp {value:,.0f}".replace(",", ".")

# The form
with st.form("my_calculator"):
    st.subheader("Enter the Product Description")
    myProductName = st.text_input("Product Name")
    myProductAmount = st.number_input('Product Amount', min_value=0, step=1)
    myJastipFeePercentage = st.number_input('Jastip Fee Percentage', min_value=0.1, max_value=0.3, step=0.1)
    submit = st.form_submit_button('Calculate!')

if submit:
    jastipFee = int(myJastipFeePercentage * myProductAmount)
    result = int(myProductAmount + jastipFee + packaging + transportFee + mealFee)
    st.write("### The total is:", format_rupiah(result))
    st.write("### Here's the detail:")
    st.write(f"- **Product Name:** {myProductName}")
    st.write(f"- **Product Amount:** {format_rupiah(int(myProductAmount))}")
    st.write(f"- **Jastip Fee:** {format_rupiah(jastipFee)}")
    st.write(f"- **Packaging:** {format_rupiah(packaging)}")
    st.write(f"- **Transport Fee:** {format_rupiah(int(transportFee))}")
    st.write(f"- **Meal Fee:** {format_rupiah(int(mealFee))}")
