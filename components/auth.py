import streamlit as st
from utilis.file_handler import read_users, add_user, user_exists

#-----------Register-------------------#
def register():
    st.subheader("Register")

    username= st.text_input("Username")
    password= st.text_input("Password", type='password')
    role = st.selectbox("Role",['job_seeker','employer'])

    if st.button("Register"):
        if username=="" or password=="":
            st.warning("Please enter username & password")
        elif user_exists(username):
            st.warning("Username already exists")
        else:
            add_user(username,password,role)
            st.success("Registered successfully! Please login.")

#----------------Login---------------
def login():
    st.subheader("Login")

    username= st.text_input("Username",key="login_user")
    password= st.text_input("Password", type='password',key='login_pass')

    if st.button("Login"):
        users=read_users()
        for user in users:
            if user['username']==username and user['password']==password:
                st.session_state['logged_in']= True
                st.session_state['username']=username
                st.session_state['role']=user['role']
                st.success(f"Logged in as {username} ({user['role']})")
                return
        st.error("Invalid username or password")
