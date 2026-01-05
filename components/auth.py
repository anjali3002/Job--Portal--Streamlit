import re
import streamlit as st
from utilis.file_handler import read_users, add_user, user_exists
import hashlib

# ---------------- Password utils ----------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# ---------------- Register ----------------
def register():
    st.subheader("Register")

    with st.form("register_form"):
        username = st.text_input("Username")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        role = st.selectbox("Role", ["job_seeker", "employer"])

        submitted = st.form_submit_button("Register")

    if submitted:
        # ---- Basic validation ----
        if not all([username, email, phone, password, confirm_password]):
            st.warning("All fields are required")
            return

        if password != confirm_password:
            st.warning("Passwords do not match")
            return

        if user_exists(username):
            st.warning("Username already exists")
            return

        # ---- Email validation ----
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_pattern, email):
            st.warning("Invalid email address")
            return

        # ---- Phone validation (digits only, 10–15 chars) ----
        if not phone.isdigit() or not (10 <= len(phone) <= 15):
            st.warning("Invalid phone number")
            return

        # ---- Save user ----
        hashed_pw = hash_password(password)
        add_user(username, hashed_pw, role, email, phone)

        st.success("Registered successfully! Please login.")
