import streamlit as st

from utilis.users import (
    validate_login,
    add_user,
    user_exists
)

from components.job_seeker import job_seeker_ui
from components.employer import employer_ui


def login_ui():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        role = validate_login(username, password)

        if role:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = role
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid username or password")


def signup_ui():
    st.title("📝 Sign Up")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["job_seeker", "employer"])

    if st.button("Create Account"):
        if not username or not password:
            st.warning("Please fill all fields")
            return

        if user_exists(username):
            st.error("Username already exists")
            return

        add_user(username, password, role)
        st.success("Account created successfully! Please login.")
        st.rerun()


def logout():
    for key in ["logged_in", "username", "role"]:
        if key in st.session_state:
            del st.session_state[key]

    st.success("Logged out successfully")
    st.rerun()


def main():
    st.sidebar.title("Job Portal")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        choice = st.sidebar.radio("Navigation", ["Login", "Sign Up"])

        if choice == "Login":
            login_ui()
        else:
            signup_ui()
    else:
        st.sidebar.write(f"👤 {st.session_state['username']}")
        if st.sidebar.button("Logout"):
            logout()

        if st.session_state["role"] == "job_seeker":
            job_seeker_ui()
        else:
            employer_ui()


if __name__ == "__main__":
    main()
