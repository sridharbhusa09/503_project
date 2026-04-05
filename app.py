import streamlit as st

# Simulated database
if "users" not in st.session_state:
    st.session_state.users = {
        "arpit": {"password": "1234", "balance": 1000}
    }

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Login function
def login(username, password):
    users = st.session_state.users
    if username in users and users[username]["password"] == password:
        st.session_state.logged_in = True
        st.session_state.current_user = username
        return True
    return False

# UI
st.title("🏦 Simple Bank App")

if not st.session_state.logged_in:
    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if login(username, password):
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")

else:
    user = st.session_state.current_user
    st.subheader(f"Welcome, {user}")

    balance = st.session_state.users[user]["balance"]
    st.write(f"💰 Balance: ₹{balance}")

    option = st.selectbox("Choose action", ["Deposit", "Withdraw", "Logout"])

    if option == "Deposit":
        amount = st.number_input("Enter amount", min_value=0)
        if st.button("Deposit"):
            st.session_state.users[user]["balance"] += amount
            st.success(f"Deposited ₹{amount}")

    elif option == "Withdraw":
        amount = st.number_input("Enter amount", min_value=0)
        if st.button("Withdraw"):
            if amount <= balance:
                st.session_state.users[user]["balance"] -= amount
                st.success(f"Withdrawn ₹{amount}")
            else:
                st.error("Insufficient balance")

    elif option == "Logout":
        st.session_state.logged_in = False
        st.experimental_rerun()