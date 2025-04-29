import streamlit as st
import pandas as pd
from datetime import datetime

# Title
st.title("📱 Mobile Recharge Ledger")

# Session state initialization
if 'ledger' not in st.session_state:
    st.session_state.ledger = pd.DataFrame(columns=['Name', 'Mobile Number', 'Amount', 'Date'])

# Recharge form
st.header("Add Recharge Entry")
with st.form("recharge_form"):
    name = st.text_input("Customer Name")
    mobile = st.text_input("Mobile Number")
    amount = st.number_input("Recharge Amount", min_value=0.0, format="%.2f")
    date = st.date_input("Recharge Date", value=datetime.today())

    submitted = st.form_submit_button("Add Recharge")
    if submitted:
        new_entry = {
            "Name": name,
            "Mobile Number": mobile,
            "Amount": amount,
            "Date": date.strftime("%Y-%m-%d")
        }
        st.session_state.ledger = pd.concat([st.session_state.ledger, pd.DataFrame([new_entry])], ignore_index=True)
        st.success("Recharge entry added!")

# Display ledger
st.header("📋 Recharge Ledger")
st.dataframe(st.session_state.ledger, use_container_width=True)
